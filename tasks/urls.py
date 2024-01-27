from django.urls import path
from django.views.decorators.cache import cache_page

from .views import TaskListView, TaskInstanceView, TaskSearchView

urlpatterns = [
    path("tasks/", (TaskListView.as_view()), name="task-list"),
    path("tasks/search/", (TaskSearchView.as_view()), name="task-search"),
    path("tasks/<int:pk>/", (TaskInstanceView.as_view()), name="task-instance"),
]