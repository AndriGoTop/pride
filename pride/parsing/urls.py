from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    #path("tool/<int:tool_id>", views.tools, name='tools'),
    path('qwerty/', views.articles_list)
]
