from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Library

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_librarian')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_librarian')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_librarian', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_librarian', 'is_staff', 'is_superuser'),
        }),
    )

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
