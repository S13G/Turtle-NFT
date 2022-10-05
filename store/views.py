from django.contrib import messages
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


# class ProductFilter(ListView):
#     template_name = 'store/product-filter.html'

#     def get_queryset(self):
#         category_id = self.kwargs['id']
#         category = Category.objects.get(id=category_id)
#         return Product.objects.filter(category__slug=slug)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         categories = Category.objects.get(id=self.kwargs['id'])
#         context["categories"] = context["categories"].filter(category=category)
#         return context
     
    # def get_queryset(self):
    #     self.products = Product.objects.select_related('category').all()
    #     self.categories = Category.objects.all()
    #     return [self.products, self.categories]
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.select_related('category').all()
    #     context['categories'] = Category.objects.all()
    #     return context
    
 
