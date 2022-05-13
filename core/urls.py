from django.urls import path
from . import views
from .views import HomeView, ProductDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
]