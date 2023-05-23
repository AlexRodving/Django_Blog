from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
	path('about/', views.about, name='about'),
    # диномическая ссылка на страницу<число:primary_key, классы из views, имя
	path('blog/<int:pk>', views.PostsView.as_view(), name='post'), 
	# Обработка форм
	path('blog/create', views.create, name='create'),
	# Rest API маршрут для всех постов
	path('api/posts/', views.api_posts),
	# Rest API маршрут для конкретного поста
	path('api/posts/<int:pk>', views.api_posts_detail)
]