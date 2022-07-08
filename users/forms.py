

from .models import Post
from django.forms import ModelForm, TextInput, Textarea, HiddenInput


class UserForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name','text']
        widgets = {
            'name': HiddenInput(attrs={
                "placeholder":"Назва"
            }),
            'text': Textarea(attrs={
                'placeholder':'Текст'
            }),

        }