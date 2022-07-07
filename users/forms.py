

from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class UserForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name','text']
        widgets = {
            'name': TextInput(attrs={
                "placeholder":"Назва"
            }),
            'text': Textarea(attrs={
                'placeholder':'Текст'
            }),

        }