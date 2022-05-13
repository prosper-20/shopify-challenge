from django.urls import path
from . import views
from .views import HomeView, ProductDetailView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('prodcut/<sslug:slug>/update/', ProductUpdateView.as_view(), name="product-update")
]