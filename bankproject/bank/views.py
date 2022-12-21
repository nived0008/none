
import django
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import MyModel

from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect





def homepage(request):



    return render(request, "homepage.html",)




def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user =auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('form')
    else:
      messages.info(request,"invalid credentials")
      return redirect('login')
  else:
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('login')

    return render(request, 'register.html')

def new(request):
    return render(request,'new.html')


def form(request):
    if request.method=="POST":
            name=request.POST['name']
            dob=request.POST['dob']
            age=request.POST['age']
            gender=request.POST['gender']
            phone=request.POST['phone']
            email=request.POST['email']
            address=request.POST['address']
            district=request.POST['district']
            branch=request.POST['branch']
            account=request.POST['account_type']
            materials=request.POST['materials']
            mymodel=MyModel(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,district=district,branch=branch,account=account,materials=materials)
            mymodel.save();

    return render(request, "form.html")


