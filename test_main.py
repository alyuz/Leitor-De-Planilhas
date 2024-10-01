from unittest import TestCase
import main


class TestePlanilhaAlunos(TestCase):
    resultados_alunos = None
    alunos_esperados = [['RA;Nome'],['123456;Diogo']]

    def setup(self):
        self.resultados_alunos = main.ler_planilha_alunos('alunos.csv')

    def test_ler_planilha(self):
        self.assertEqual(self.resultados_alunos, self.alunos_esperados)

    def test_alunos_is_list(self):
        self.assertIsInstance(self.resultados_alunos, list)
