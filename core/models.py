from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=10)


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    libros = models.ManyToManyField(Libro, related_name="authors", blank=True)



class Rating(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveSmallIntegerField()
