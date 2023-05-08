from .models import Post #Класс описание модели БД
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea 

class PostForm(ModelForm):               #Класс формы наследуем от класса форм Джанго
    class Meta:                                 
        model = Post                     #Указывваем модель БД
        fields = ['title','anons','text','date'] #Поля из БД

        widgets = {                        #Описание полей формы формат ключ: значение
            "title": TextInput(attrs={
                'placeholder': 'Название'  #Вложенный обьет для атрибутов поля формы,
            }),                            #здесь то что в скобках у html - id,class,placeholder
             "anons": TextInput(attrs={
                'placeholder': 'Анонс'
            }),
             "text": Textarea(attrs={
                'placeholder': 'Текст статьи'
            }),
             "date": DateTimeInput(attrs={
                'placeholder': 'год-месяц-день час:минуты:секунды'
            }),
        }