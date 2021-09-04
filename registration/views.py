from django import forms
from django.shortcuts import render
from .forms import OredrForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def registration(request):
    form = OredrForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)