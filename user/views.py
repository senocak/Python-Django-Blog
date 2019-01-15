from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        auth_login(request,newUser)
        return redirect("index")
    context = {
        "form":form
    }
    return render(request,"register.html",context)
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            auth_login(request,newUser)
            return redirect("index")
        context = {
            "form":form
        }
        return render(request,"register.html",context)

    else:
        form = RegisterForm()
        context = {
            "form":form
        }
        return render(request,"register.html",context)
    """

def login(request):
    return render(request,"login.html")

def logout(request):
    pass