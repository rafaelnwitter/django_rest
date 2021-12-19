from django.http import response
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Teste numero 1 cria curso', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Teste numero 2 cria curso', nivel='A'
        )

    def test_req_get_lista_cursos(self):
        """Teste para verificar se a requisição GET de cursos esta certa"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_req_post_cria_cursos(self):
        """Teste para verificar a criação via POST de um novo curso"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'TEST 3',
            'nivel': 'B'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_req_delete_cursos(self):
        """
        Teste para verificar a remoção via DELETE de um curso.
        Sómente usuarios com permissões com essa autenticação podem fazer essa ação
        """
        response = self.client.delete('/cursos/2/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_req_put_atualiza_cursos(self):
        """Teste para verificar a atualização via PUT de um novo curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'TEST 1 atualizado',
            'nivel': 'A'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
