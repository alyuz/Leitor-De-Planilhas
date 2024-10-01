from unittest import TestCase
import main2


class Test(TestCase):
    resultado_real = None
    resultado_referencia = [['UF;Nome'],['SP;Campinas'],['SP;Valinhos'],['SP;Indaiatuba']]

    def setUp(self):
        self.resultado_real = main2.ler_arquivo_csv('cidades.csv')

    def test_ler_arquivo_csv(self):
        self.assertEqual(self.resultado_real,self.resultado_referencia)

    def test_multiplicacao(self):
        res1 = main2.multiplicacao(2, 10)
        self.assertEqual(res1, 20)
