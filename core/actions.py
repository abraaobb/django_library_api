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
