from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class HomeView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "core/home.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    
