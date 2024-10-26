from django.urls import path
from . import views

urlpatterns = [
    #path("home", views.home_views),
    path("products/", views.parsing_site),
]
