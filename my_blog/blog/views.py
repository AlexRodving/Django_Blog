from django.shortcuts import render, redirect #redirect - перенаправление на страницу
from .models import Post
from django.views.generic import DetailView #подключить для динамических страниц
from .forms import PostForm                 #импорт формы из forms.py

# Create your views here.

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

def home(request):
    return render(request, 'blog/index.html')

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