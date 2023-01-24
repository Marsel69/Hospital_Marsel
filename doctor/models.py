from django.db import models

# Create your models here.
class Direction(models.Model):
    title = models.CharField(max_length=255, verbose_name='Направление')

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направлении"
    def __str__(self):
        return self.title

class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    datetime = models.DateField(verbose_name='Год рождения')
    experience = models.IntegerField(verbose_name='Стаж')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Направление')

    class Meta:
        verbose_name = "информация о докторе"
        verbose_name_plural = "Добавить доктора"

    def __str__(self):
        return self.name
