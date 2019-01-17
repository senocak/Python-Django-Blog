from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import ArticleForms
from .models import Article, Comment
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
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

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

def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
    #return redirect("/articles/article/"+str(id))
    return redirect(reverse("article:detail",kwargs={"id":id}))
