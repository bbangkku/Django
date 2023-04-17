from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('throw/', views.throw, name= 'throw'),
    path('catch/', views.catch, name = 'catch'),
    path('articles/', views.articles, name='articles'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
]
