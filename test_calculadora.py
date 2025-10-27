import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_somar_funciona(self):
        self.assertEqual(calculadora.somar(1, 2), 3)

    def test_subtrair_funciona(self):
        self.assertEqual(calculadora.subtrair(5, 3), 2)
    
    def test_multiplicar_funciona(self):
        self.assertEqual(calculadora.multiplicar(3, 4), 12)    

    def test_dividir_funciona(self):
        self.assertEqual(calculadora.dividir(2, 2), 1)    
