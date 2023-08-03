# in urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot.html/', views.chatbot, name='chatbot.html'),
    path('word/', views.word, name='word'),
]

