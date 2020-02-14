from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
 
# Create your models here.
class Post(models.Model):
    def default_datetime(): return timezone.now()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chequeAmount = models.CharField(max_length=200, help_text='Сумма чека*', verbose_name='На какую сумму у вас есть чек?')
    chequeDate = models.CharField(max_length=100, help_text='Дата совершения покупки',)
    chequeThing = models.CharField(max_length=200, help_text='Товар*', verbose_name='Вещи которые вы купили?')
    shop = models.IntegerField(default=1, verbose_name='Магазин', help_text='Откуда вы купили товар?',) 
    date = models.DateTimeField(default=default_datetime, verbose_name='Дата добавления чека')

