from django.db import models

# Create your models here.

class CostumUser(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    repassword  =models.CharField(max_length=50)