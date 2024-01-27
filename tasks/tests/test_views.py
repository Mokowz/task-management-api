from tasks.models import Task, Tag
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse


class TaskTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            title = "Test Title",
            description = 'Test Description',
            completed = True,
            created_at = '2024-01-01',
            updated_at = '2024-01-04',
            priority = 'high',
            due_date = '2024-01-10',
        )
        self.task.tags.add(self.tag)

        self.task2 = Task.objects.create(
            title = "Test Title 2",
            description = 'Test Description 2',
            completed = False,
            created_at = '2024-04-01',
            updated_at = '2024-05-04',
            priority = 'low',
            due_date = '2024-08-10',
        )
        self.task2.tags.add(self.tag)

    # test tasks list view (GET Method)
    def test_task_list_get_view(self):
        url = reverse('task-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], "Test Title")
        # self.assertEqual(response.data[0]["tags"], "Test Tag")
        self.assertEqual(response.data[0]["due_date"], "2024-01-10")

    # Filter functionality
    def test_task_list_filter_by_priority(self):
        url = reverse("task-list")
        response = self.client.get(url, {"priority": "low"})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Title 2")

    # By completed
    def test_task_list_filter_by_completed(self):
        url = reverse("task-list")
        response = self.client.get(url, {"completed": False})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Title 2")

    


