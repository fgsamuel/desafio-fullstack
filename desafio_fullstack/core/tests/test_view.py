from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from desafio_fullstack.core.models import Estado, Cidade


class EstadoViewTestCase(TestCase):
    def setUp(self):
        self.url_list = reverse('core:estados_list')
        self.url_create = reverse('core:estados_create')
        self.estado = Estado.objects.create(sigla='MG', nome='Minas Gerais')
        self.url_update = reverse('core:estados_update', kwargs={'estado_pk': self.estado.id})
        self.url_delete = reverse('core:estados_delete', kwargs={'estado_pk': self.estado.id})
        # login
        User.objects.create_superuser('usuario', '', 'usuario')
        self.client.login(username='usuario', password='usuario')

    def test_url_list_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)

    def test_busca(self):
        """Ao buscar um estado ele deve ser apresentado na tela"""
        dados = dict(pesquisa='minas')
        resp = self.client.post(self.url_list, dados)
        self.assertContains(resp, 'Minas Gerais')

    def test_busca_sem_resultado(self):
        """Ao buscar um estado que não existe ele deve apresentar mensagem"""
        dados = dict(pesquisa='teste')
        resp = self.client.post(self.url_list, dados)
        self.assertContains(resp, 'Nenhum estado encontrado.')

    def test_url_create_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)

    def test_cadastro(self):
        """Ao receber um post deve salvar os dados"""
        dados = dict(sigla='PR', nome='Paraná')
        self.client.post(self.url_create, dados)
        existe = Estado.objects.filter(nome='Paraná').exists()
        self.assertTrue(existe)

    def test_url_update_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_update)
        self.assertEqual(resp.status_code, 200)

    def test_alteracao(self):
        """Ao receber um post deve alterar os dados do estado"""
        dados = dict(sigla='MG', nome='Minas')
        self.client.post(self.url_update, dados)
        estado_alterado = Estado.objects.filter(nome__iexact='Minas').exists()
        self.assertTrue(estado_alterado)

    def test_url_delete_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_delete)
        self.assertEqual(resp.status_code, 200)

    def test_apagar(self):
        """Ao receber um post deve apagar"""
        self.client.post(self.url_delete)
        estado_apagado = Estado.objects.filter(nome='Minas Gerais').exists()
        self.assertFalse(estado_apagado)


class CidadeViewTestCase(TestCase):
    def setUp(self):
        self.url_list = reverse('core:cidades_list')
        self.url_create = reverse('core:cidades_create')
        self.estado = Estado.objects.create(sigla='MG', nome='Minas Gerais')
        self.cidade = Cidade.objects.create(estado=self.estado, nome='Belo Horizonte')
        self.url_update = reverse('core:cidades_update', kwargs={'cidade_pk': self.cidade.id})
        self.url_delete = reverse('core:cidades_delete', kwargs={'cidade_pk': self.cidade.id})
        # login
        User.objects.create_superuser('usuario', '', 'usuario')
        self.client.login(username='usuario', password='usuario')

    def test_url_list_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)

    def test_busca(self):
        """Ao buscar uma cidade ela deve ser apresentado na tela"""
        dados = dict(pesquisa='Belo')
        resp = self.client.post(self.url_list, dados)
        self.assertContains(resp, 'Belo Horizonte')

    def test_busca_sem_resultado(self):
        """Ao buscar uma cidade que não existe ele deve apresentar mensagem"""
        dados = dict(pesquisa='teste')
        resp = self.client.post(self.url_list, dados)
        self.assertContains(resp, 'Nenhuma cidade encontrada.')

    def test_url_create_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)

    def test_cadastro(self):
        """Ao receber um post deve salvar os dados"""
        dados = dict(estado=self.estado.id, nome='Uberlândia')
        resp = self.client.post(self.url_create, dados)
        existe = Cidade.objects.filter(nome='Uberlândia').exists()
        self.assertTrue(existe)

    def test_url_update_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_update)
        self.assertEqual(resp.status_code, 200)

    def test_alteracao(self):
        """Ao receber um post deve alterar os dados da cidade"""
        dados = dict(estado=self.estado.id, nome='Novo nome')
        self.client.post(self.url_update, dados)
        cidade_alterada = Cidade.objects.filter(nome__iexact='Novo nome').exists()
        self.assertTrue(cidade_alterada)

    def test_url_delete_sucesso(self):
        """A url deve retornar status 200"""
        resp = self.client.get(self.url_delete)
        self.assertEqual(resp.status_code, 200)

    def test_apagar(self):
        """Ao receber um post deve apagar"""
        self.client.post(self.url_delete)
        cidade_apagada = Cidade.objects.filter(nome='Belo Horizonte').exists()
        estado_existe = Estado.objects.filter(id=self.estado.id).exists()
        self.assertFalse(cidade_apagada)
        self.assertTrue(estado_existe)




