from modulefinder import Module

from django.db import models

class Tools(models.Model):
    image_tool = models.ImageField(upload_to='intro_pictures/%Y/%m/%d', verbose_name='Обложка') # будет подгружать картинку инструмента
    title = models.CharField(max_length=30, verbose_name="Название") # название инструмента
    price_ym = models.IntegerField(verbose_name="Цена яндекс маркет") # цена яндекс маркет
    price_ozon = models.IntegerField(verbose_name="Цена ozon") # цена озон
    price_wb = models.IntegerField(verbose_name="Цена вб") # цена вб
    url_ym = models.URLField(verbose_name="url яндекс маркет") # url на яндекс маркет
    url_ozon = models.URLField(verbose_name="url ozon")  # url на ozon
    url_wb = models.URLField(verbose_name="url wb")  # url на wb
    # еще нужно откуда то взять

    def __str__(self):
        return self.title