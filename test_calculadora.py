import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_somar_funciona(self):
        self.assertEqual(calculadora.somar(1, 2), 3)

