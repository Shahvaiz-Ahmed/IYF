from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from home.models import ContactUs
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


# login
def loginuser(request):
    if request.method == 'POST':
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(username=username , password=password)
         if user is not None:
            login(request,user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("/")
         else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', context={
        "login_form":form
    })


# registration

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("index")
        else:
            form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form':form})
    

# home 

def index(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request, "index.html")


# objectives

def objective(request):
    return render(request, "objective.html")


# contact form

def contactUs(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        tellme = request.POST.get('tellme')
        contactus = ContactUs(fname='fname', lname='lname', email='email', tellme='tellme')
        contactus.save()
    return render(request, "contactUs.html")


# logout


def logoutuser(request):
    logout(request)
    return render(request, "login.html")