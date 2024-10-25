from modulefinder import Module

from django.db import models

class Tools(models.Model):
    image_tool = models.ImageField(upload_to='intro_pictures/%Y/%m/%d', verbose_name='Обложка') # будет подгружать картинку инструмента
    title = models.CharField(max_length=30) # название инструмента
    price_ym = models.IntegerField() # цена яндекс маркет
    price_ozon = models.IntegerField() # цена озон
    price_wb = models.IntegerField() # цена вб
    url_ym = models.URLField() # url на яндекс маркет
    url_ozon = models.URLField()  # url на ozon
    url_wb = models.URLField()  # url на wb
    # еще нужно откуда то взять

    def __str__(self):
        return self.title