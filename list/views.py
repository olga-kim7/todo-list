from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View

from list.forms import TaskForm, CompleteForm
from list.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "list/tag_list.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "list/task_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["CompleteForm"] = CompleteForm()
        return context


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:index")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class AssignUserToTaskView(View):

    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('list:index')
