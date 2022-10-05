from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from setting.models import Settings
from store.models import Product, Category

import os

# Create your views here.


class CategoryList(ListView):
    model = Category
    template_name = 'store/category.html'
    context_object_name = 'category'


class ProductDetail(DetailView):
    model = Product
    template_name = 'store/product-detail.html'

# Product Listing
def product_list(request):
    products_list = Product.objects.select_related('category').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 5)

    # Page Pagination
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    #passing website settings dummy stats
    Settings.objects.get_or_create(id=1)
    
    context = {"products": products}
    context['settings'] = Settings.objects.first()

    if context['settings']:
        os.environ['web_name'] = context['settings'].title
    return render(request, 'store/index.html', context)

# Category filter
def category_view(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        messages.warning("No Such Category")
    products = category.products.all()
    context = {"products": products, "category": category}
    return render(request, "store/product-filter.html", context)

# search query
def search_view(request):
    results = []
    if request.method == "GET":
        query = request.GET.get("q")
        if query == '':
            query = 'None'
        results = Product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query) | Q(description__icontains=query))
    context = {"query": query, "results": results}
    return render(request, 'store/search.html', context)
   