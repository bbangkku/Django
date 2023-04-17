
from django.contrib import admin
from django.urls import path,include
from myapp2 import views

app_name = 'myapp2'
urlpatterns = [
    path('calculation/',views.calculation, name='calculation'),
    # path('<int:num1>&<int:num2>/',views.calculation),
    path('result/',views.result, name='result'),
]
