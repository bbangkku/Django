
from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('', views.index),
    # /myapps/숫자/형태로 URL이구성되어 있다면, detail 함수로 라우팅
    # *주의사항 : 괄호랑 콜론 등 모두 띄어쓰기 하지 말기
    # 항상 / << 붙여줘야함 마지막에
    path('<int:number>/', views.detail)
]
