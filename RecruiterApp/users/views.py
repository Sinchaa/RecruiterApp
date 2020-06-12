from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm,LoginForm,EmailVerifyForm

# Create your views here.

def home(request):
    return render(request,'home.html')


def reg(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            print(name,email,password)

    form = RegistrationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email,password)
    form = LoginForm()
    return render(request,'login.html',{'form':form})

def emailVerify(request):
    if request.method=='POST':
        form = EmailVerifyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email,password)
    form = EmailVerifyForm()
    return render(request,'emailVerify.html',{'form':form})

def about(request):
    return render(request,'about.html')