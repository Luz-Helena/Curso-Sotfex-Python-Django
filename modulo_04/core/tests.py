from django.test import TestCase, Client
from django.contrib.auth.models import User
from projects.models import Project
from .models import Tarefa

class TarefaCreationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.project = Project.objects.create(user=self.user, titulo='Test Project')
        self.client.login(username='testuser', password='password')

    def test_create_tarefa_success(self):
        response = self.client.post('/', {
            'titulo': 'New Task',
            'project': self.project.id
        })
        # If successful, it should redirect to home
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tarefa.objects.filter(titulo='New Task').exists())
