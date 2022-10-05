from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from store.models import Product, Category

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'store/index.html'
    paginate_by = 2
    context_object_name= 'products'


class CategoryList(ListView):
    model = Category
    template_name = 'store/category.html'
    context_object_name = 'category'


class ProductDetail(DetailView):
    model = Product
    template_name = 'store/product-detail.html'


def CategoryViews(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        messages.warning("No Such Category")
    products = category.products.all()
    context = {"products": products, "category": category}
    return render(request, "store/product-filter.html", context)


def SearchView(request):
    results = []
    if request.method == "GET":
        query = request.GET.get("q")
        if query == '':
            query = 'None'
        results = Product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query) | Q(description__icontains=query))
    context = {"query": query, "results": results}
    return render(request, 'store/search.html', context)
   