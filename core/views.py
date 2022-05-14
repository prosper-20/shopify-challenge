from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class HomeView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "core/home.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["brand", "category", "name", "code", "image", "quantity", "rate", "status", "seller", "slug"]


    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class MakeProduct(CreateView):
    model = Product
    fields = ["brand", "category", "name", "code", "image", "quantity", "rate", "status", "seller", "slug"]




class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ["brand", "category", "name", "code", "image", "quantity", "rate", "status", "seller", "slug"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False


