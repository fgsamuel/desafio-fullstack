from django.test import TestCase

from desafio_fullstack.core.forms import EstadoForm, CidadeForm
from desafio_fullstack.core.models import Estado


class EstadoFormTestCase(TestCase):
    def test_normalize_sigla(self):
        """Ao salvar os dados é preciso colocar a sigla em maiúsculo"""
        data = dict(sigla='mg', nome='Minas Gerais')
        form = EstadoForm(data)
        form.is_valid()
        self.assertEqual(form.cleaned_data['sigla'], 'MG')

    def test_normalize_nome(self):
        """Ao salvar os dados é preciso colocar o nome com as primeiras letras maiúsculas e as demais minúsculas"""
        data = dict(sigla='MG', nome='minas gerais')
        form = EstadoForm(data)
        form.is_valid()
        self.assertEqual(form.cleaned_data['nome'], 'Minas Gerais')


class CidadeFormTestCase(TestCase):
    def test_normalize_nome(self):
        """Ao salvar os dados é preciso colocar o nome com as primeiras letras maiúsculas e as demais minúsculas"""
        estado = Estado.objects.create(sigla='MG', nome='Minas Gerais')
        data = dict(estado=estado, nome='belo HORIZONTE')
        form = CidadeForm(data)
        form.is_valid()
        self.assertEqual(form.cleaned_data['nome'], 'Belo Horizonte')
