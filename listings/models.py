from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Band(models.Model):
    def __str__(self):
        return f' {self.name}'
    

    class Genre(models.TextChoices):
        Local = 'lc'
        Importé = 'ip'
   
   
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField( max_length=1000)
    recipe = models.fields.CharField( max_length=5000)
    #official_homepage = models.fields.URLField(null=True, blank=True)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)


class Listing(models.Model):
    def __str__(self):
        return f' {self.name}'
    

    class Types(models.TextChoices):
        sucrée = 'su'
        fermentée = 'fe'
        alcoolisée = 'al'

    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField( max_length=1000)
    recipe = models.fields.CharField( max_length=5000)

    sold = models.fields.BooleanField(default=True)
    type = models.fields.CharField(choices=Types.choices, max_length=5)


class Desert(models.Model):
    def __str__(self):
        return f' {self.name}'
    

    class category(models.TextChoices):
        Blé = 'bl'
        maïs = 'ma'
        arachides = 'ar'

    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField( max_length=1000)
    recipe = models.fields.CharField( max_length=5000)

    sold = models.fields.BooleanField(default=True)
    type = models.fields.CharField(choices=category.choices, max_length=5)

class home(models.Model):
    def __str__(self):
        return f' {self.name}'



class Chat(models.Model):
    content = models.CharField(max_length=500, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' {self.content}'