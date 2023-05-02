from django.shortcuts import render

# Create your views here.

posts = [
	{
    	'author': 'Администратор',
    	'title': 'Это первый пост',
    	'content': 'Содержание первого поста.',
    	'date_posted': '12 мая, 2022'
	},
	{
    	'author': 'Пользователь',
    	'title': 'Это второй пост',
    	'content': 'Подробное содержание второго поста.',
    	'date_posted': '13 мая, 2022'
	}
]

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def blog(request): 
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)
