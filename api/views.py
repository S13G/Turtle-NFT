from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from api.serializers import ProductSerializer

from store.models import Category, Product, Transaction

# Create your views here.


class ProductList(ListAPIView):
    filter_backends = (SearchFilter,)
    queryset = Product.objects.select_related('category').order_by('-added_on').all()
    search_fields = ['name', 'price', 'token', 'category__name']
    serializer_class = ProductSerializer


class CategoryList(APIView):
    def get(self, request):
        try:
            categories = Category.objects.values('id', 'name')
        except Category.DoesNotExist:
            return Response('No category has been added')
        return Response(categories, status=200)


class CategoryProduct(APIView):
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return Response('Category Does Not Exist')
        category_products = category.products.values('id', 'name', 'category', 'image', 'token', 'price')
        return Response(category_products, status=200)


class ProductTransaction(APIView):
    def get(self, request):
        try:
            transactions = Transaction.objects.values('id', 'discord_link', 'wallet_address', 'product_id')
        except Transaction.DoesNotExist:
            return Response('No transactions to show')
        return Response(transactions, status=200)