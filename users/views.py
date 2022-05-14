from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        passowrd = request.POST['password']
        password2 = request.POST['password2']

        if passowrd == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!!")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email belongs to another user")
                return redirect("register")
            else:
                User.objects.create_user(username=username, email=email, passowrd=password)
                messages.success(request, f"Hi {username}, your account creation was successful, Kindly login below")
                return redirect("login")
        else:
            messages.error(request, "Both password fields didn't match")
            return redirect("register")
    return render(request, "users/register.html")
            
