from django.urls import path

from store.views import marketplace, category_view, CategoryList, search_view, main_page


urlpatterns = [
    path('', main_page, name="main-page"),
    path('marketplace/', marketplace, name='marketplace'),
    path('category/', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>', category_view, name='category-filter'),
    path('search/', search_view, name="search")
]
