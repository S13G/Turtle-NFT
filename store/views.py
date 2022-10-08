from django.contrib import messages
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
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
    products_list = Product.objects.select_related('category').order_by('price').all()
    categories = Category.objects.all()
    connect_button = request.POST.get("connect")
    buy_button = request.POST.get("buy")
    if connect_button:
        messages.info(request, "Not available")
    elif buy_button:
        messages.error(request, "Not available")
    
    # Page Pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 16)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {"products": products, "categories": categories}
    return render(request, 'store/marketplace.html', context)


# Category filter
def category_view(request, slug):
    categories = Category.objects.all()
    buy_button = request.POST.get("buy")
    if buy_button:
        messages.error(request, "Not available")
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        messages.info("No Such Category")
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
    connect_button = request.POST.get("connect")
    if connect_button:
        messages.info(request, "Not available")

    context = {"settings": Settings.objects.first(), "connect_button": connect_button}

    if context['settings']:
        os.environ['web_name'] = context['settings'].trade_mark
    return render(request, 'base.html', context)