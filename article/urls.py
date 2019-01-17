from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('', views.index, name="article_index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/article/', views.create_article, name="create_article"),
    path('article/<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('comment/<int:id>/', views.addComment, name="comment"), 
]