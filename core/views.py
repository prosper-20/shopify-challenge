from typing import List
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Comment, Warehouse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from core.forms import CommentForm, WarehouseForm
from django.contrib import messages

# Create your views here.


class HomeView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "core/home2.html" # Changed from home.html to home2.html
    paginate_by = 3


# class ProductDetailView(DetailView):
#     model = Product
#     context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["brand", "category", "name", "code", "image",
              "quantity", "rate", "status", "seller", "slug"]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class MakeProduct(CreateView):
    model = Product
    fields = ["brand", "category", "name", "code", "image",
              "quantity", "rate", "status", "seller", "slug"]


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["brand", "category", "name", "code", "image",
              "quantity", "rate", "status", "seller", "slug"]

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     product = self.get_object()
    #     if self.request.user == product.seller:
    #         return True
    #     return False


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'

    # def test_func(self):
    #     product = self.get_object()
    #     if self.request.user == product.seller:
    #         return True
    #     return False


class UserProductListView(ListView):
    model = Product
    template_name = 'core/user_products.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('seller'))
        return Product.objects.filter(seller=user).order_by('-name')


class ProductCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    # success_url = "/"
    template_name = "core/product_comment_form.html"

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'slug': self.kwargs['slug']})



def ProductDetailView(request, slug=None): # < here
    product = get_object_or_404(Product, slug=slug) # < here
    products = Product.objects.all()[:2]
    if request.method == "POST":
        name = request.POST["name"]
        body = request.POST["body"]

        new = Comment.objects.create(product=product, name=name, body=body)
        new.save()
        messages.success(request, "Comment saved")
        return redirect("/")
        
    else:
        form = CommentForm()
        # You changed form product_detail.html to detail_2.html to product-page.html
        return render(request, 'core/product-page.html', {"product": product, "products": products})

    
def PhoneView(request):
    products = Product.objects.filter(category="1").all()
    return render(request, "core/available.html", {"products": products})


def ElectronicsView(request):
    products = Product.objects.filter(category="2").all()
    return render(request, "core/electronics.html", {"products": products})


def OtherView(request):
    products = Product.objects.filter(category="3").all()
    return render(request, "core/other.html", {"products": products})


class Warehouse(CreateView):
    model = Warehouse

    form_class = WarehouseForm
    # success_url = "/"
    template_name = "core/warehouse_form.html"

