from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    published_year = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Library(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return f"Biblioteca de {self.owner.username}"