import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_somar_funciona(self):
        self.assertEqual(calculadora.somar(1, 2), 3)

    # Note que a função 'subtrair' ainda não tem teste aqui! 
    # Ela será a linha vermelha no Coveralls, gerando os 88%.
    # Para o propósito da demonstração, não a incluímos.