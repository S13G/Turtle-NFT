from django.urls import path

from api.views import ProductList, CategoryList


urlpatterns = [
    path('products/', ProductList.as_view()),
    path('category/', CategoryList.as_view())
]
