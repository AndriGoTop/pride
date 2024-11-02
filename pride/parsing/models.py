from enum import unique
from modulefinder import Module
from django.utils import timezone
from django.db import models

class Tools(models.Model):
    image = models.ImageField(upload_to='intro_pictures', verbose_name='Обложка') # будет подгружать картинку инструмента
    name = models.CharField(max_length=30, verbose_name="Название") # название инструмента
    price = models.CharField(max_length=10, verbose_name="Цена") # название инструмента
    # price_ozon = models.IntegerField(verbose_name="Цена ozon") # цена озон
    # price_wb = models.IntegerField(verbose_name="Цена вб") # цена вб
    url = models.CharField(max_length=255, verbose_name="url", unique=True) # url на яндекс маркет
    # url_ozon = models.URLField(verbose_name="url ozon")  # url на ozon
    # url_wb = models.URLField(verbose_name="url wb")  # url на wb)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # Установка значения по умолчанию
    # еще нужно откуда то взять

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интсрумент'
        verbose_name_plural = 'Инструменты'
        ordering = ['-created_at']
