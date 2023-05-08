from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
	path('about/', views.about, name='about'),
    # диномическая ссылка на страницу<число:primary_key, классы из views, имя
	path('blog/<int:pk>', views.PostsView.as_view(), name='post'), 
	# Обработка форм
	path('blog/create', views.create, name='create')
]