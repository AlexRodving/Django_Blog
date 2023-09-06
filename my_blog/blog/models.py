from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    img = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
