from django import forms
from .models import Todo

class TodoPost(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['item']