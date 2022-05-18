from django.urls import path
from .views import (HomeView, 
ProductDetailView, 
ProductCreateView, 
ProductUpdateView, 
ProductDeleteView, 
MakeProduct,
UserProductListView, 
ProductCommentView,
PhoneView,
ElectronicsView,
OtherView,
Warehouse,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('product/phones/', PhoneView, name="phones"),
    path('product/electronics/', ElectronicsView, name="electronics"),
    path("product/other/", OtherView, name='other'),
    path("product/<slug:slug>/", ProductDetailView, name="product-detail"),
    path('user/<str:seller>/', UserProductListView.as_view(), name='user-products'),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('product/<slug:slug>/delete/', ProductDeleteView.as_view(), name="product-delete"),
    path('new/', MakeProduct.as_view(), name="maker"),
    path('product/<slug:slug>/comment/', ProductCommentView.as_view(), name="post_comments"),
    path('warehouse/create/', Warehouse.as_view(), name="warehouse")
    
]

