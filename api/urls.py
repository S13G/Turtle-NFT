from django.urls import path

from api.views import ProductList, CategoryList, CategoryProduct


urlpatterns = [
    path('products/', ProductList.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<slug:slug>', CategoryProduct.as_view())
]
