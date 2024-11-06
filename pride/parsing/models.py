from enum import unique
from modulefinder import Module
from django.utils import timezone
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)  # Уникальный идентификатор товара
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интсрумент'
        verbose_name_plural = 'Инструменты'
        ordering = ['-created_at']
