from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from setting.models import Settings
from store.models import Product, Category

import os

# Create your views here.


class CategoryList(ListView):
    model = Category
    template_name = 'store/category.html'
    context_object_name = 'category'


# Product Listing
def marketplace(request):
    products = Product.objects.select_related('category').all()
    categories = Category.objects.all()
    context = {"products": products, "categories": categories}
    return render(request, 'store/marketplace.html', context)


# Category filter
def category_view(request, slug):
    categories = Category.objects.all()
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        messages.warning("No Such Category")
    products = category.products.all()
    context = {"products": products,
               "categories": categories, "category": category}
    return render(request, "store/marketplace-filter.html", context)


# search query
def search_view(request):
    categories = Category.objects.all()
    results = []
    if request.method == "GET":
        query = request.GET.get("search")
        if query == '':
            query = 'None'
        results = Product.objects.filter(Q(name__icontains=query) | 
        Q(price__icontains=query) | Q(token__icontains=query))
    context = {"query": query, "results": results, "categories": categories}
    return render(request, 'store/search-item.html', context)


def main_page(request):
    Settings.objects.get_or_create(id=1)

    context = {"settings": Settings.objects.first()}

    if context['settings']:
        os.environ['web_name'] = context['settings'].trade_mark
    return render(request, 'base.html')
