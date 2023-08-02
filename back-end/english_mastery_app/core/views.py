from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def chatbot(request):
    return HttpResponse("Chatbot Page")

def word(request):
    return HttpResponse("Word of the Day Page")
