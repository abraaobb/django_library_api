from rest_framework import serializers
from .models import User, Book, Library

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_librarian']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LibrarySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Library
        fields = ['id', 'owner', 'books']