from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Category, Product

# Create your views here.


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').values(
            'id', 'name', 'category', 'image', 'token', 'price')
        return Response(products, status=200)


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.values('id', 'name')        
        return Response(categories, status=200)
