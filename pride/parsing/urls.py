from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("tool/<int:tool_id>", views.tools, name='tools'),
    path("products/", views.parsing_site),
    path('qwerty/', views.news_view)
]
