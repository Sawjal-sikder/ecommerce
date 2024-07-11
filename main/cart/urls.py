from django.urls import path
from . import views
urlpatterns = [
    path('shop_cart/', views.shop_cart, name='shop_cart'),
]
