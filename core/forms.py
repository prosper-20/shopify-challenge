import imp
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Warehouse


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ["name", "body"]


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse

        fields = ["name", 'location', 'item', 'date_stored']
