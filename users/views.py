from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!!")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email belongs to another user")
                return redirect("register")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, f"Hi {username}, your account creation was successful, Kindly login below")
                return redirect("login")
        else:
            messages.error(request, "Both password fields didn't match")
            return redirect("register")
    return render(request, "users/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in")
            return redirect('/')
        else:
            messages.error(request, "Credentials not valid")
            return redirect("login")
    #You changed from login.htnl to form-login
    return render(request, 'users/login.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
            
