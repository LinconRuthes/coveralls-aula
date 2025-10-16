import unittest
from calculadora import somar, subtrair

class TestCalculadora(unittest.TestCase):
    
    def test_soma_simples(self):
        # TESTE 1: Cobre a função 'somar'
        self.assertEqual(somar(2, 3), 5)

    def test_subtracao_caso_a_maior(self):
        # TESTE 2: Cobre a condição 'if a > b' da função 'subtrair'
        self.assertEqual(subtrair(5, 2), 3)