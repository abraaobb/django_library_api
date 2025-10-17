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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed_by')
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'book', 'returned_at')

    def __str__(self):
        return f"{self.user.username} → {self.book.title}"
