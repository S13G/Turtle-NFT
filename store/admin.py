from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


from store.models import Product, Category, Transaction

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_on'
    list_display = ['name', 'category', 'price', 'transactions_count']
    list_per_page = 10
    list_select_related = ['category']
    ordering = ['name', 'category']
    prepopulated_fields = {'slug': ['name']}
    readonly_fields = ['added_on', 'updated_on']
    search_fields = ['name__istartswith', 'category__name']

    @admin.display(ordering='transactions_count')
    def transactions_count(self, product):
        url = reverse('admin:store_transaction_changelist') + \
            '?' + urlencode({'product__id': str(product.id)})
        return format_html('<a href="{}">{}</a>', url, product.transactions_count)

    def get_queryset(self, request):
        return super(ProductAdmin, self).get_queryset(request).annotate(transactions_count=Count('transaction'))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name']

    def has_add_permission(self, request):
        return False if self.get_queryset(request).count() == 7 else True


@admin.register(Transaction)
class Transactions(admin.ModelAdmin):
    list_display = ['discord_link', 'wallet_address', 'product_id']
    readonly_fields = ['discord_link', 'wallet_address']
    search_fields = ['discord_link', 'product_id', 'block_hash']

    def has_add_permission(self, request):
        return False
