
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse

def ex_data(req,data):
    return req.POST.get(data,"")

def index(request):
    if request.POST:
        username = ex_data(request,"username")
        password = ex_data(request,"password")
        print(username,password)
        user = User.objects.get(username=username)
        print(user.password)
        user= authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user=user)
            return redirect('hos')
        else:
            messages.info(request,'Invalid')
            return redirect('login') 
    else:
        return render(request,'login.html')

def go(request):
    if request.POST:
        username = ex_data(request,"username")
        password = ex_data(request,"password")
        print(username,password)
        user = User.objects.get(username=username)
        print(user.password)
        user= authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user=user)
            return redirect('hos')
        else:
            messages.info(request,'Invalid')
            return redirect('login') 
    else:
        return render(request,'login.html')

def hospital(request):
    return render(request, 'hospital.html') 

def prediction(request):
    return prediction(request,'prediction.html')    
def out(request):
    logout(request)
    return redirect('login')       

def signup(request):
    
    if request.POST:
        hospital_name = ex_data(request,"hospital_name")
        hospital_id = ex_data(request,"hospital_id")
        license_id = ex_data(request,"license_id")
        email_id = ex_data(request,"email_id")
        
        
        
        try:
            user = User(username=hospital_name,email=email_id,password=license_id)
            # user.password=license_id
            user.set_password(license_id)
            user.save()
            print(user.password)
            return redirect(go)
        except Exception as e:
            messages.success(request,str(e))
    return render(request,'signup.html')    
