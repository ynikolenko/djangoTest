from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    price = models.TextField('Price')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'