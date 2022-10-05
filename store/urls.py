from django.urls import path

from store.views import ProductList, ProductDetail, CategoryViews, CategoryList


urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('category/', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>', CategoryViews, name='category-filter'),
]
