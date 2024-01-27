from django.urls import path
from django.views.decorators.cache import cache_page

from .views import TaskListView, TaskInstanceView, TaskSearchView

urlpatterns = [
    path("tasks/", (TaskListView.as_view()), name="task-list"),
    path("tasks/search/", cache_page(60 * 20)(TaskSearchView.as_view()), name="task-search"),
    path("tasks/<int:pk>/", cache_page(60 * 20)(TaskInstanceView.as_view()), name="task"),
]