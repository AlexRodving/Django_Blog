from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post                     #Указывваем модель БД
        fields = ['id','title','anons','text','date','img'] #Поля из БД
