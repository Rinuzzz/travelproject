from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        u = request.POST['username']
        p = request.POST['password']
        user=auth.authenticate(username=u,password=p)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        x = request.POST['username']
        y = request.POST['first_name']
        z = request.POST['last_name']
        a = request.POST['email']
        b = request.POST['password']
        c = request.POST['password1']
        if b==c:
            if User.objects.filter(username=x).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=a).exists():
                 messages.info(request,"Email Taken")
                 return redirect('register')
            else:
                user=User.objects.create_user(username=x,password=b,first_name=y,last_name=z,email=a)
                user.save();
                return redirect('login')
                # print("User Register")
        else:
             messages.info(request,"password not matching")
             return redirect('register')
        # return redirect('/')
            # print("password not matching")
    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')