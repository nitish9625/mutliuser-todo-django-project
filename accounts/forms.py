from django import forms
from django.forms import fields
from django.forms import ModelForm
from .models import Todo


class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ('title', 'desc', 'status', 'priority')


