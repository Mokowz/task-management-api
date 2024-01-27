from tasks.models import Task, Tag
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse


class TaskListTestCase(TestCase):
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


# Test the instance view
class TaskInstanceTestView(TestCase):
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

    # Test the viewing function
    def test_task_instance_get(self):
        url = reverse("task-instance", kwargs={"pk": self.task.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # Test the update functionality
    def test_task_instance_update(self):
        url = reverse("task-instance", kwargs={"pk": self.task.pk})
        data = {
            "title": "Updated Title",
            "description": "Dummy description",
            "completed": False,
            "due_date": "2024-01-01",
            "tags": self.tag.pk
        }
        response = self.client.put(url, data)
        print(f"URL: {url}")
        print(f"Response: {response}")
        print(f"Response Data: {response.data}")

        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Title")
    
    # Test deletion
    def test_task_instance_delete(self):
        url = reverse("task-instance", kwargs={"pk": self.task.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)


