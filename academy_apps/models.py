from django.db import models


class Carausel(models.Model):
    image = models.ImageField('Картинка', upload_to = 'image/')
    title = models.CharField('Загловок', max_length = 255)
    text = models.CharField('Краткая биография', max_length= 255, null=True, blank=True)

    class Meta():
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.title
