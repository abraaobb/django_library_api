from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Library
from core import actions
import unittest

User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser', email='test@example.com', password='12345')
        self.assertEqual(user.username, 'testuser')
        self.assertFalse(user.is_librarian)
        self.assertTrue(user.check_password('12345'))

    def test_create_librarian(self):
        librarian = User.objects.create_user(
            username='libuser', email='lib@example.com', password='12345', is_librarian=True)
        self.assertTrue(librarian.is_librarian)


class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Django for APIs',
            author='William Vincent',
            published_year=2023,
            available=True
        )

    def test_book_str(self):
        self.assertEqual(str(self.book), 'Django for APIs')

    def test_book_availability(self):
        self.assertTrue(self.book.available)


class LibraryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='owner', email='owner@example.com', password='12345')
        self.book1 = Book.objects.create(
            title='Book 1', author='Author A', published_year=2022)
        self.book2 = Book.objects.create(
            title='Book 2', author='Author B', published_year=2021)
        self.library = Library.objects.create(owner=self.user)
        self.library.books.set([self.book1, self.book2])

    def test_library_books(self):
        self.assertEqual(self.library.books.count(), 2)

    def test_library_str(self):
        self.assertEqual(str(self.library.owner), 'owner')


class LibraryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='apiuser', email='api@example.com', password='12345')
        self.library = Library.objects.create(owner=self.user)
        self.book = Book.objects.create(
            title='Book API', author='API Author', published_year=2024)
        self.library.books.add(self.book)

        self.client.force_authenticate(user=self.user)

    def test_get_libraries(self):
        response = self.client.get('/api/libraries/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCalculadora(TestCase):

    def setUp(self):
        self.calc = actions.Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 5), 15)

    def test_dividir(self):
        self.assertAlmostEqual(self.calc.dividir(10, 2), 5.0)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


class CalculadoraAvancadaTest(unittest.TestCase):
    """Classe de testes unitários para a Calculadora."""

    def setUp(self):
        """Executado antes de cada teste: cria uma instância da Calculadora."""
        self.calc = actions.Calculadora()

    def test_potencia(self):
        """Verifica se a potência é calculada corretamente."""
        resultado = self.calc.potencia(2, 3)
        self.assertEqual(resultado, 8)

    def test_raiz_quadrada(self):
        """Verifica se a raiz quadrada de um número positivo é correta."""
        resultado = self.calc.raiz_quadrada(9)
        self.assertEqual(resultado, 3.0)

    def test_raiz_quadrada_negativo(self):
        """Verifica se ocorre erro ao calcular raiz quadrada de número negativo."""
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-4)


class TestAtividade9(TestCase):
    """Testes para a classe Atividade9 definida em core.actions."""

    def setUp(self):
        self.atividade = actions.Atividade9()

    def test_is_pair_even(self):
        """Números pares devem retornar True."""
        self.assertTrue(self.atividade.is_pair(4))
        self.assertTrue(self.atividade.is_pair(0))

    def test_is_pair_odd(self):
        """Números ímpares devem retornar False."""
        self.assertFalse(self.atividade.is_pair(7))
        self.assertFalse(self.atividade.is_pair(-3))

    def test_get_average_normal(self):
        """Média de lista de números é calculada corretamente."""
        self.assertAlmostEqual(self.atividade.get_average([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(self.atividade.get_average([1.5, 2.5]), 2.0)

    def test_get_average_empty_raises(self):
        """Chamar get_average com lista vazia levanta ValueError."""
        with self.assertRaises(ValueError):
            self.atividade.get_average([])


if __name__ == "__main__":
    # Executa todos os testes da classe
    unittest.main()
