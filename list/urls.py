from django.urls import path
from list.views import (
    TaskListView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    AssignUserToTaskView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/assign/", AssignUserToTaskView.as_view(), name="task-assign"),

]

app_name = "list"
