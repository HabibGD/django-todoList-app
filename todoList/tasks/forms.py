from django import forms
from .models import TaskTodo


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = TaskTodo
        fields = ["title", "description"]
