from datetime import date
from django import forms
from django.db import models
from django.forms import CharField, EmailField, PasswordInput, RadioSelect

# Create your models here.
class ContactUs(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=15)
    tellme = models.TextField(max_length=150)

def __str__(self):
    return self.fname
