"""first_pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views
urlpatterns = [
    # 127.0.0.1:8000/admin/ 으로 요청을 보냈을 때 응답한다.
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/admin/ 으로 요청이 오면 views.index를 실행한다.
    path('articles/', views.index),
    path('firstapp/', views.templates),
    path('firstapp/first/', views.templates_first),
    path('firstapp/first2/', views.first),
    path('firstapp/homework1_2/', views.homework1_2),
]
