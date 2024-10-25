from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('index', views.index, name='index'),
    path('tool', views.tool, name='tool'),
]