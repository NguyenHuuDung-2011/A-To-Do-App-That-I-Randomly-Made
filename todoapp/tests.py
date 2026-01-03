from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class TodoItemModelTest(TestCase):
    def setUp(self):
        TodoItem.objects.create(title="Test Task 1", description="This is a test task.", completed=False)

    def test_todo_item_creation(self):
        task = TodoItem.objects.get(title="Test Task 1")
        expected_description = f"{task.description}"
        self.assertEqual(expected_description, "This is a test task.")

class TodoPageViewTest(TestCase):
    def setUp(self):
        TodoItem.objects.create(title="Test Task 2", description="Another test task.")

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