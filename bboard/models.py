from django.db import models


class Bb(models.Model):
    """Объявление"""
    title = models.CharField(verbose_name='Товар', max_length=50)
    content = models.TextField(
        verbose_name='Описание', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    published = models.DateTimeField(
        verbose_name='Опубликовано', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']
