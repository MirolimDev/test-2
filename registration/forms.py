from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from django.forms import ModelForm

from .models import CostumUser

class OredrForm(ModelForm):
    class Meta:
        model = CostumUser
        fields = '__all__'

