from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

def HomePage(request):
    return render(request,'users/homepage.html')

def loginPage(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            messages.info(request,f"{request.POST['username']} sucessfully logged in")
            return redirect('users:homepage')
        else:
            messages.error(request,'User does not exists')
            return redirect(request,'users:homepage')
    else:
        return render(request,'users/login.html')

@login_required
def logoutpage(request):
    auth.logout(request)
    print(f"user {{user.username}} ogged out")
    return redirect('/')

def register(request):
    """Resister new user"""
    if request.method == 'POST':
        data = [request.POST['username'],request.POST['password1'],request.POST['email']]
        # if password is not maching
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.create_user(username=data[0],password=data[1],email=data[2])
            user.save()
            login(request,user)
            return redirect('users:homepage')
    else:
        return render(request,'users/sign_in.html')