from django.urls import path

from store.views import product_list, ProductDetail, category_view, CategoryList, search_view


urlpatterns = [
    path('', product_list, name='products'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('category/', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>', category_view, name='category-filter'),
    path('search/', search_view, name="search")
]
