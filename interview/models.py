from django.db import models


class Interview(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание')
    date_start = models.DateField(verbose_name='Дата старта', auto_now_add=True, auto_now=False, editable=False)
    date_end = models.DateField(verbose_name='Дата окончания')
