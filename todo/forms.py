from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    """
    Making my own form.
    """
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
