from django.urls import path

from . import views
from django.conf import settings



urlpatterns = [
    path('<category_slug>/', views.ProductList, name='ProductListByCategory'),
    path('<id>/<slug>/', views.ProductDetail, name='ProductDetail'),
    path('', views.ProductList, name='ProductList'),
]
