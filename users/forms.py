import imp
from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User


        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile


        fields = ["image"]