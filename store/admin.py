from django.contrib import admin

from store.models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
    date_hierarchy = 'added_on'
    list_display = ['name', 'category', 'price']
    list_per_page = 10
    list_select_related = ['category']
    ordering = ['name', 'category']
    prepopulated_fields = {'slug': ['name']}
    readonly_fields = ['added_on', 'updated_on']
    search_fields = ['name__istartswith', 'category__istartswith']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name']

    def has_add_permission(self, request):
        return False if self.get_queryset(request).count() == 7 else True