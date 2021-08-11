from django.contrib.admin import AdminSite
from django.test import TestCase

from desafio_fullstack.core.admin import EstadoAdmin, CidadeAdmin
from desafio_fullstack.core.forms import EstadoForm, CidadeForm
from desafio_fullstack.core.models import Estado, Cidade


class EstadoAdminTestCase(TestCase):
    def setUp(self):
        site = AdminSite()
        self.admin = EstadoAdmin(Estado, site)

    def test_list_display(self):
        """Deve exibir os campos sigla e nome"""
        self.assertTupleEqual(self.admin.list_display, ('sigla', 'nome'))

    def test_search_fields(self):
        """Deve ser possível pesquisar pela sigla e pelo nome"""
        self.assertTupleEqual(self.admin.search_fields, ('sigla', 'nome'))

    def test_form(self):
        """Deve utilizar o EstadoForm"""
        self.assertEqual(self.admin.form, EstadoForm)


class CidadeAdminTestCase(TestCase):
    def setUp(self):
        site = AdminSite()
        self.admin = CidadeAdmin(Cidade, site)

    def test_list_display(self):
        """Deve exibir os campos nome e estado (get_estado)"""
        self.assertTupleEqual(self.admin.list_display, ('nome', 'get_estado'))

    def test_search_fields(self):
        """Deve ser possível pesquisar pelo nome e pelo estado (estado__nome)"""
        self.assertTupleEqual(self.admin.search_fields, ('nome', 'estado__nome'))

    def test_form(self):
        """Deve utilizar o CidadeForm"""
        self.assertEqual(self.admin.form, CidadeForm)
