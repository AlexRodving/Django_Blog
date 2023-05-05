from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
	path('about/', views.about, name='about'),
	path('blog/<int:pk>', views.PostsView.as_view(), name='post'), 
	# диномическая ссылка на страницу<число:primary_key, классы из views, имя
]