# in urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot.html/', views.chatbot, name='chatbot.html'),
    path('word/', views.word, name='word'),
    path('api/wordoftheday/', views.WordOfTheDayListCreateView.as_view(), name='wordoftheday_list_create'),
    path('api/chatmessage/', views.ChatMessageListCreateView.as_view(), name='chatmessage_list_create'),
    path('oauth_test/', views.oauth_test, name='oauth_test'),

]

