from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Library

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_librarian')
    list_filter = ('is_staff', 'is_librarian', 'is_superuser')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_year', 'available')
    search_fields = ('title', 'author')
    list_filter = ('available', 'published_year')

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner')
    search_fields = ('owner__username',)
    filter_horizontal = ('books',)  # para selecionar múltiplos livros facilmente
