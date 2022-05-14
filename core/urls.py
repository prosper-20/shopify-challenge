from django.urls import path
from . import views
from .views import HomeView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, MakeProduct

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('product/<slug:slug>/delete/', ProductDeleteView.as_view(), name="product-delete"),
    path('new/', MakeProduct.as_view(), name="maker")
]

