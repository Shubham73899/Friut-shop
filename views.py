from django.shortcuts import render, redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout , login, authenticate
# from django.contrib.messages import messages

# Create your views here.
def home(request):
    #get all the rows from product table in db
    products= Product.objects.all()
    categories = Category.objects.all()
    return render(request,'index.html',{'products':products ,"categories":categories })

def product(request,id):
    product = Product.objects.get(id = id)


    realted_products= Product.objects.filter(category=product.category).exclude(id=id)[:4]
    return render(request,'product.html',{'product' : product  , 'realted_products' : realted_products  })

def catgory(request, id):
    if id=="all":
        categories = Category.objects.all()
        for items in categories:
            product_count = Product.objects.filter(category = items).count()
            items.product_count = product_count
        products = Product.objects.all()    
        return render(request, 'category.html' , {"categories":categories , 'products':products})
    categories = Category.objects.all()  
    products = Product.objects.filter(category=id)    
    return render(request, 'category.html' , {"categories":categories , 'products':products})



def login_user(request):
    if request.POST:
        email=request.POST['username']
        password=request.POST['password']
             
        log_user=authenticate(username=email,password=password) 
        user=User.objects.filter(username=email).exists()

        if not user:
            return render(request,'login.html',{'msg1':"Enter valid username"})
        
        if  log_user is not None:
            login(request,log_user)
            return redirect('home')
        
        else:
            return render(request,'login.html',{'msg1':"Enter valid password"})

    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect ('login')

def signup(request):
    if request.POST:
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        exists=User.objects.filter(username= email).exists()

        if exists:
            return render(request,'signup.html',{'msg2':'Email already exists'})
        new_user= User.objects.create_user(first_name= firstname,  last_name =lastname ,username= email, password= password)
        new_user.save()

        return redirect('login')

    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')
