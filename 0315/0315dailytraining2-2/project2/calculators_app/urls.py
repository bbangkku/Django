from django.contrib import admin
from django.urls import path,include
from calculators_app import views
urlpatterns = [
    path('<int:number1>/<int:number2>/', views.detail),
]
