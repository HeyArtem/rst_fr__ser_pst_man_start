from tabnanny import verbose
from turtle import update
from django.db import models
import datetime
from django.core.validators import MinValueValidator
from decimal import Decimal


# функция заменит имя медиафайла на текущую дату
def blog_img_directory_path(instance, filename):
    today = datetime.datetime.today
    filename = f"{instance.title}.{filename.split('.')[-1]}"
    
    return f"blog/{today.year}/{today.month}/{today.day}/{filename}"


# модель девушки без картинок, без many to many
class HairColor(models.Model):
    title = models.CharField(verbose_name='Цвет волос', max_length=25)
    
    class Meta:
        verbose_name = 'Цвет волос'
        verbose_name_plural = 'Цвет волос'
    
    def __str__(self) -> str:
        return self.title

class Girls(models.Model):
    
    STATUS_GIRL = (
        ('married', 'Замужем'),
        ('unmarried', 'Незамужняя')
    )
    
    name = models.CharField(verbose_name='Имя', max_length=20)
    hair_color = models.ForeignKey(HairColor, verbose_name='Цвет волос', on_delete=models.SET_NULL, null=True)
    growth = models.PositiveBigIntegerField(verbose_name='Рост')
    weight = models.DecimalField(verbose_name='Вес', max_digits=3, decimal_places=0, validators=[MinValueValidator(Decimal('0.01'))])
    girls_description = models.CharField(verbose_name='Краткое описание', max_length=300, unique=True)
    phone = models.PositiveIntegerField(verbose_name='Контактный телефон', default=88002000500)
    listing_date = models.DateTimeField(verbose_name='Дата внесения в базу', auto_now_add=True)
    update_list_date = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    status = models.CharField(verbose_name='Статус', choices=STATUS_GIRL, default='unmarried', max_length=25)
    
    class Meta:
        verbose_name = 'Девушка'
        verbose_name_plural = 'Девушки'
    
    # магический метод, что бы выводились имена моделей
    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"


