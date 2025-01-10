<<<<<<< HEAD
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .forms import Signupforms, Seller_Account_Form, Upload_product, Comment_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Create_Seller_Account ,Products, Comments      

def home(request):
    return render(request,'layout/home.html')

def  detection(request):
    return render(request,'layout/des.html')

def ecommerce(request):
    has_seller_account=Create_Seller_Account.objects.filter(user=request.user).exists()
    
    return render(request,'layout/e_home.html',{'has_seller_account':has_seller_account})


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
            seller_account = form.save(user=request.user,commit=False)  # Don't save yet
            seller_account.user = request.user  # Set the logged-in user
            seller_account.save()  # Now save it
            messages.success(request, "Your seller account has been created successfully.")
            return redirect('home')
        else:
            messages.error(request, "There was an error in the form. Please correct it.")
    else:
        form = Seller_Account_Form()

   

    return render(request, 'layout/selleracc.html', {"form": form})
    


def profile(request):
    Seller_Account=Create_Seller_Account.objects.get(user=request.user)
    data={"Seller_Account":Seller_Account}
    return render(request,'layout/profile.html',data)

def products(request):
    products=Products.objects.all()
    seller=Create_Seller_Account.objects.all()
    
    data={"products":products,"seller":seller}
    return render(request,'layout/products.html',data)


def product_forms(request):
    if request.method=='POST':
        product=Upload_product(request.POST,request.FILES)
        
        if product.is_valid():
            seller=Create_Seller_Account.objects.get(user=request.user)
            product.save(user=request.user,seller=seller)
            return redirect('products')
        else:
            print(product.errors)
    else:
        product=Upload_product()
        print("form not submitted or invalid !!")
         
    return render(request,'layout/product_form.html',{'form':product})

def product_details(request,pk=None):
    product_det=Products.objects.get(id=pk)
    comments= Comments.objects.filter(product=product_det)
    if request.method=='POST':
        comment=Comment_form(request.POST)
        if comment.is_valid():
            comment.save(user=request.user,product=product_det)
            return redirect('product_details',pk=pk)
        else:
            print(comment.errors)
    else:
        comment=Comment_form()
    data={"products_det":product_det,'form':comment,'Comments':comments}
=======
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .forms import Signupforms, Seller_Account_Form, Upload_product
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Create_Seller_Account ,Products       

def home(request):
    return render(request,'layout/home.html')

def  detection(request):
    return render(request,'layout/des.html')

def ecommerce(request):
    has_seller_account=Create_Seller_Account.objects.filter(user=request.user).exists()
    
    return render(request,'layout/e_home.html',{'has_seller_account':has_seller_account})


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
            seller_account = form.save(user=request.user,commit=False)  # Don't save yet
            seller_account.user = request.user  # Set the logged-in user
            seller_account.save()  # Now save it
            messages.success(request, "Your seller account has been created successfully.")
            return redirect('home')
        else:
            messages.error(request, "There was an error in the form. Please correct it.")
    else:
        form = Seller_Account_Form()

   

    return render(request, 'layout/selleracc.html', {"form": form})
    


def profile(request):
    Seller_Account=Create_Seller_Account.objects.get(user=request.user)
    data={"Seller_Account":Seller_Account}
    return render(request,'layout/profile.html',data)

def products(request):
    products=Products.objects.all()
    seller=Create_Seller_Account.objects.all()
    
    data={"products":products,"seller":seller}
    return render(request,'layout/products.html',data)


def product_forms(request):
    if request.method=='POST':
        product=Upload_product(request.POST,request.FILES)
        
        if product.is_valid():
            seller=Create_Seller_Account.objects.get(user=request.user)
            product.save(user=request.user,seller=seller)
            return redirect('products')
        else:
            print(product.errors)
    else:
        product=Upload_product()
        print("form not submitted or invalid !!")
         
    return render(request,'layout/product_form.html',{'form':product})

def product_details(request,pk=None):
    product_det=Products.objects.get(id=pk)
    data={"products_det":product_det}
>>>>>>> 235f43ea45fb7904dfdbcdba5ee43e48947246b1
    return render(request,'layout/product_det.html',data)