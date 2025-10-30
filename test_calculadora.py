import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_somar_funciona(self):
        self.assertEqual(calculadora.somar(1, 2), 3)

    def test_subtrair_funciona(self):
        self.assertEqual(calculadora.subtrair(3, 2), 1)

    def test_multiplica_funciona(self):
        self.assertEqual(calculadora.multiplicar(3, 2), 6)

    def test_dividir_funciona(self):
        self.assertEqual(calculadora.dividir(3, 3), 1)