from django.core.exceptions import ValidationError
from django.test import TestCase

from desafio_fullstack.core.models import Estado, Cidade


class EstadoTestCase(TestCase):
    """Deve retornar o nome do estado"""
    def test_str(self):
        estado = Estado(sigla='MG', nome='Minas Gerais')
        self.assertEqual(str(estado), 'Minas Gerais')

    def test_estado_duplicado(self):
        """Não pode permitir uma cidade com sigla duplicada"""
        Estado.objects.create(sigla='MG', nome='Minas Gerais')
        estado = Estado(sigla='MG', nome='Minas Gerais')
        self.assertRaises(ValidationError, estado.full_clean)

    def test_sigla_quantidade(self):
        """A sigla do estado não pode conter menos de dois caracteres"""
        estado = Estado(sigla='M', nome='Minas Gerais')
        self.assertRaises(ValidationError, estado.full_clean)


class CidadeTestCase(TestCase):
    """Deve retornar o nome no formato <nome cidade> (<sigla estado>)"""
    def test_str(self):
        estado = Estado.objects.create(sigla='MG', nome='Minas Gerais')
        cidade = Cidade(estado=estado, nome='Belo Horizonte')
        self.assertEqual(str(cidade), 'Belo Horizonte (MG)')

    def test_cidade_duplicada(self):
        """Não pode cadastrar duas ciades com o mesmo nome no mesmo estado"""
        estado = Estado.objects.create(sigla='MG', nome='Minas Gerais')
        Cidade.objects.create(estado=estado, nome='Belo Horizonte')
        cidade = Cidade(estado=estado, nome='Belo Horizonte')
        self.assertRaises(ValidationError, cidade.full_clean)
