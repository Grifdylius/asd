from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


# class Post(models.Model):
#     title = models.CharField('Title' ,max_length=150)
#     slug = models.SlugField('Link' ,max_length=150, unique=True)
#     image = models.ImageField('Photo', blank = True, null = True)
#     content = models.TextField('Text')
#     date = models.DateField('Publication date', default = timezone.now)
#     publish = models.BooleanField('Publish', default = False)
    
#     def get_link(self):
#         return reverse('post_detail_url', kwargs={'slug':self.slug})
    
#     class Meta():
#         verbose_name = 'News'
#         verbose_name_plural = 'News'

#     def __str__(self):
#         return self.title

# class Post_rus(models.Model):
#     title = models.CharField('Заголовок' ,max_length=150)
#     slug = models.SlugField('Ссылка' ,max_length=150, unique=True)
#     image = models.ImageField('Фото', blank = True, null = True)
#     content = models.TextField('Текст')
#     date = models.DateField('Дата публикации', default = timezone.now)
#     publish = models.BooleanField('Опубликовано', default = False)

#     def get_link_ru(self):
#         return reverse('post_detail_ru_url', kwargs={'slug':self.slug})
#     class Meta():
#         verbose_name = 'Новость'
#         verbose_name_plural = 'Новости'

#     def __str__(self):
#         return self.title

class Carausel(models.Model):
    image = models.ImageField('Картинка', upload_to = 'image/')
    title = models.CharField('Загловок', max_length = 255)
    text = models.CharField('Краткая биография', max_length= 255, null=True, blank=True)

    class Meta():
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.title
