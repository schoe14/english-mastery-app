from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import WordOfTheDaySerializer, ChatMessageSerializer
from .models import WordOfTheDay, ChatMessage
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages

class WordOfTheDayListCreateView(generics.ListCreateAPIView):
    queryset = WordOfTheDay.objects.all()
    serializer_class = WordOfTheDaySerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
def home(request):
    if request.user.is_authenticated:
        messages.success(request, 'Welcome back, {}'.format(request.user.username))
    context = {'message': 'Welcome to English Mastery App!'}
    return render(request, 'core/home.html', context)


def chatbot(request):
    return render(request, 'core/chatbot.html.html')

def word(request):
    return render(request, 'core/word.html')

def oauth_test(request):
    return render(request, 'core/oauth_test.html')
