from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post                     #Указывваем модель БД
        fields = ['title','anons','text','date'] #Поля из БД