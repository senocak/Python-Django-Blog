from django.shortcuts import render, HttpResponse

def index(request):

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def article(request,id):
    return HttpResponse("Article"+str(id))

    