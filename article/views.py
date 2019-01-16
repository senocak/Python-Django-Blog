from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForms
from .models import Article
from django.contrib import messages

def index(request):
    articles = Article.objects.all().filter(author=request.user)
    return render(request,"index.html",{"articles":articles})

def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    #articles = Article.object.filter(author=request.user)
    articles = Article.objects.all().filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def create_article(request):
    form = ArticleForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarıyla Oluşturuldu")
        return redirect("article:dashboard")
    return render(request,"create_article.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)
    context={
        "article":article
    }
    return render(request,"detail.html",context)

@login_required(login_url = "user:login")
def update(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForms(request.POST or None, request.FILES or None, instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarıyla Güncellendi")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url = "user:login")
def delete(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request, "Makale Başarıyla Silindi")
    return redirect("article:dashboard")