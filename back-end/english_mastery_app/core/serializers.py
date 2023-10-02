# serializers.py

from rest_framework import serializers
from .models import WordOfTheDay, ChatMessage

class WordOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WordOfTheDay
        fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
