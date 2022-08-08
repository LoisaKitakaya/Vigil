from django.urls import path
from . import views

# urls here
urlpatterns = [
    path('', views.home, name='home-page'),
    path('subscribe/', views.subscribe, name="subscribe"),
]