from django.shortcuts import render, redirect #redirect - перенаправление на страницу
from .models import Post
from django.views.generic import DetailView #подключить для динамических страниц
from .forms import PostForm                 #импорт формы из forms.py
import requests                             #для отправки запросов
# from django.http import JsonResponse      #Rest Api    
from .serializers import PostSerializer    #Rest Api  сериализатор
from rest_framework.response import Response#Rest Api 
from rest_framework.decorators import api_view#Rest Api 
from rest_framework import status

# Create your views here.
BASE_URL = 'https://dummyjson.com/products'
# posts = [
# 	{
#     	'author': 'Администратор',
#     	'title': 'Это первый пост',
#     	'content': 'Содержание первого поста.',
#     	'date_posted': '12 мая, 2022'
# 	},
# 	{
#     	'author': 'Пользователь',
#     	'title': 'Это второй пост',
#     	'content': 'Подробное содержание второго поста.',
#     	'date_posted': '13 мая, 2022'
# 	}
# ]

#Rest API Контроллер, использующий сериализатор для вывода постов через JSON REsponce
# def api_posts(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return JsonResponse(serializer.data, safe=False)

#Rest API Контроллер реализующий веб-представление Json, через Response
@api_view(['GET', 'POST'])
def api_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_posts_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def home(request):
    response = requests.get(f"{BASE_URL}") #GET запрос
    resp = {
        'resp': response.json()
    }
    return render(request, 'blog/index.html', resp)

def about(request):
    return render(request, 'blog/about.html')

def blog(request): 
    # context = {
    #     'posts': posts
    # }
    posts = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/blog.html', posts)

class PostsView(DetailView): # Класс динамических страниц,наслед. от DetailView
    model = Post             # Указать модель с которой работаем
    template_name = 'blog/post.html' #Указать какой шаблон будет обрабатывать
    context_object_name = 'post' #Ключ для передачи в шаблон

def create(request): #FORM
    error = ''                          #Для Ошибок
    if request.method == 'POST':        #Если метод POST
        form = PostForm(request.POST)   #буфер для проверки формы со страницы
        if form.is_valid():             #валидация формы
            form.save()                 #Сохранение формы
            return redirect('blog')     #Редирект
        else:
            error = 'Данные не верны'   #Иначе в пустую ошибку ложим значение

    form = PostForm()                   #ложим нашу форму в переменную

    data = {                            #Обьект с формой и ошибкой для передачи на страницу
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)