from django.db import models


class Bb(models.Model):
    """Объявления"""
    title = models.CharField(verbose_name='Товар', max_length=50)
    content = models.TextField(
        verbose_name='Описание', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    published = models.DateTimeField(
        verbose_name='Опубликовано', auto_now_add=True, db_index=True)
    rubric = models.ForeignKey(
        'Rubric', verbose_name='Рубрика', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Rubric(models.Model):
    """Рубрики"""
    name = models.CharField(
        verbose_name='Название', max_length=20, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

    def __str__(self):
        return self.name
