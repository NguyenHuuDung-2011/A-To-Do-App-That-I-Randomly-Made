from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your tests here.
class TodoItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester',
            password='1234'
        )

        TodoItem.objects.create(title="Test Task 1", description="This is a test task.", completed=False, user=self.user)

    def test_todo_item_creation(self):
        task = TodoItem.objects.get(title="Test Task 1")
        expected_description = f"{task.description}"
        self.assertEqual(expected_description, "This is a test task.")

class TodoPageViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester2',
            password='1234'
        )

        self.client.login(username='tester2', password='1234')

        TodoItem.objects.create(title="Test Task 2", description="Another test task.", user=self.user)

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo.html')

class AuthTest(TestCase):
    def setUp(self):
        self.testusername = 'testuser1'
        self.testpassword = 'abcd'
        User.objects.create_user(
            username=self.testusername,
            password=self.testpassword
        )

    def test_create_account_successfully(self):
        self.assertTrue(
            User.objects.filter(username=self.testusername).exists()
        )
    def test_login_account_successfully(self):
        response = self.client.post(reverse('login'), {'username': self.testusername, 'password': self.testpassword})

        self.assertEqual(response.status_code, 302)

        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)