from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_view, name='product'),
    path('success/', views.success, name='success')
]