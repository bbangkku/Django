
from django.contrib import admin
from django.urls import path,include
from calculators_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculators_app/', include('calculators_app.urls'))
]
