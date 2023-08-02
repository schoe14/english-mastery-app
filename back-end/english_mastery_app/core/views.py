from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {'message': 'Welcome to English Mastery App!'}
    return render(request, 'core/home.html', context)

def chatbot(request):
    return render(request, 'core/chatbot.html.html')

def word(request):
    return render(request, 'core/word.html')
