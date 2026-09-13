from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/no-cors/hello', views.hello_no_cors),
    path('api/cors/hello', views.hello_cors),
]
