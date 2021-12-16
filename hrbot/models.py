from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', db_index=True)
    address = models.CharField(max_length=255, verbose_name='Adress', null=True, blank=True)
    latitude = models.FloatField(verbose_name="Latitude", validators=[MaxValueValidator(90), MinValueValidator(-90)], null = True, blank=True)
    longitude = models.FloatField(verbose_name="Longitude", validators=[MaxValueValidator(180), MinValueValidator(-180)], null = True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Сities"

class Work(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    town = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    interview = models.CharField(max_length=1000, verbose_name='Interview', null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Works"
