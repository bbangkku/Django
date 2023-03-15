
from django.contrib import admin
from django.urls import path,include
from pricesapp import views
urlpatterns = [
    path('<str:name1>/<int:num>/', views.index)
]
