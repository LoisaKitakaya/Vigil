from django.urls import path
from . import views

# your urls here
urlpatterns = [
    path('', views.all_products, name="all-products"),
    path('search/', views.search_filter, name="query-product"),
    path('tag/<slug:slug>/', views.tag_filter, name="tag-filter"),
    path('<slug:slug>/', views.single_product, name="single-product"),
    path('category/<slug:slug>/', views.category_filter, name="category-filter"),
]