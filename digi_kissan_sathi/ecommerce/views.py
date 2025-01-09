from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .forms import Signupforms, Seller_Account_Form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm                

def home(request):
    return render(request,'layout/home.html')

def  detection(request):
    return render(request,'layout/des.html')

def ecommerce(request):
    return render(request,'layout/e_home.html')


def sign_up(request):
    if request.method=="POST":
        form=Signupforms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"your account has been created Successfully")
            return redirect('login_user')
        else:
            messages.error(request,"There was an error with your submission.Please try again")
    else:
        form=Signupforms() 
    return render(request,"layout/signup.html",{'form':form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  
            if user is not None:
                login(request, user)
                messages.success(request, "User has been successfully logged in!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "layout/login.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect('login_user')

def seller_account(request):
    if request.method == "POST":
        form = Seller_Account_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)  # Pass the logged-in user
            messages.success(request, "Your seller account has been created successfully.")
            return redirect('home')
        else:
            messages.error(request, "There was an error in the form. Please correct it.")
    else:
        form = Seller_Account_Form()

    return render(request, 'layout/selleracc.html', {"form": form})