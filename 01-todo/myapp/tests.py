from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoModelTest(TestCase):
	def test_create_todo(self):
		t = Todo.objects.create(title='Test Todo', description='A test')
		self.assertEqual(Todo.objects.count(), 1)
		self.assertFalse(t.resolved)


class TodoViewsTest(TestCase):
	def setUp(self):
		self.todo = Todo.objects.create(title='Task 1', description='Desc')

	def test_list_view(self):
		resp = self.client.get(reverse('myapp:todo_list'))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, self.todo.title)

	def test_create_view(self):
		resp = self.client.post(reverse('myapp:todo_create'), {'title': 'New Task', 'description': 'abc'}, follow=True)
		self.assertEqual(resp.status_code, 200)
		self.assertTrue(Todo.objects.filter(title='New Task').exists())

	def test_edit_view(self):
		resp = self.client.post(reverse('myapp:todo_edit', args=[self.todo.pk]), {'title': 'Updated', 'description': 'new'}, follow=True)
		self.todo.refresh_from_db()
		self.assertEqual(self.todo.title, 'Updated')

	def test_toggle_view(self):
		self.assertFalse(self.todo.resolved)
		resp = self.client.get(reverse('myapp:todo_toggle', args=[self.todo.pk]), follow=True)
		self.todo.refresh_from_db()
		self.assertTrue(self.todo.resolved)

	def test_delete_view(self):
		resp = self.client.post(reverse('myapp:todo_delete', args=[self.todo.pk]), follow=True)
		self.assertFalse(Todo.objects.filter(pk=self.todo.pk).exists())

