import math


class Calculadora:
    def somar(self, a: int, b: int) -> int:
        return a + b

    def subtrair(self, a: int, b: int) -> int:
        return a - b

    def multiplicar(self, a: int, b: int) -> int:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

        # NOVA FUNÇÃO 1
    def potencia(self, base: int, expoente: int) -> float:
        """Calcula a potência (base elevado ao expoente)."""
        return math.pow(base, expoente)

    # NOVA FUNÇÃO 2
    def raiz_quadrada(self, numero: float) -> float:
        """Calcula a raiz quadrada de um número positivo."""
        if numero < 0:
            raise ValueError(
                "Não é possível calcular raiz quadrada de número negativo.")
        return math.sqrt(numero)


class ConversorTemperatura:
    """Classe responsável pela conversão de temperaturas entre Celsius e Fahrenheit."""

    def celsius_para_fahrenheit(self, c: float) -> float:
        """
        Converte uma temperatura em Celsius para Fahrenheit.
        Fórmula: F = (C * 9/5) + 32
        """
        return (c * 9 / 5) + 32

    def fahrenheit_para_celsius(self, f: float) -> float:
        """
        Converte uma temperatura em Fahrenheit para Celsius.
        Fórmula: C = (F - 32) * 5/9
        """
        return (f - 32) * 5 / 9
