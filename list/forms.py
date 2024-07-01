from django import forms
from django.utils import timezone
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

    def form_valid(self, form):
        form.instance.created_at = timezone.now()
        return super().form_valid(form)


class CompleteForm(forms.Form):
    task_id = forms.IntegerField(widget=forms.TextInput(
        attrs={"class": "form-control"}))
