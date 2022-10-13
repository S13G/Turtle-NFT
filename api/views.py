from operator import truth
from urllib.parse import parse_qs, urlparse
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from api.serializers import ProductSerializer, TransactionSerializer

from store.models import Category, Product, Transaction

# Create your views here.


class ProductList(ListAPIView):
    filter_backends = (SearchFilter,)
    queryset = Product.objects.select_related(
        'category').order_by('-added_on').all()
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
        category_products = category.products.values(
            'id', 'name', 'category', 'image', 'token', 'price')
        return Response(category_products, status=200)


class ProductTransaction(APIView):

     def post(self, request):
        data = request.data
        infos = ['block_hash', 'discord_link', 'wallet_address', 'product_id']
        if set(infos) == set(data.keys()) and not None in data.values() and not "" in data.values():
            try:
                product = Product.objects.get(id=data.get('product_id'))
            except Product.DoesNotExist:
                return Response('There\'s no product with that id', status=400)
            Transaction.objects.create(block_hash=data.get('block_hash'), discord_link=data.get('discord_link'),
            wallet_address=data.get('wallet_address'), product=product)
            return Response('Transaction successful', status=200)
        else:
            return Response("Fields not filled properly or a field is missing", status=400)