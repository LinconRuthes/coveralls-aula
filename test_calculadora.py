import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_somar_funciona(self):
        self.assertEqual(calculadora.somar(1, 2), 3)

    # NOVO TESTE: Para cobrir a função subtrair
    def test_subtrair_funciona(self):
        self.assertEqual(calculadora.subtrair(5, 3), 2) # <-- Esta linha vai tocar o return de subtrair