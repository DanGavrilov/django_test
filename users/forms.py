from .models import Post, Information
from django.forms import ModelForm, TextInput, Textarea, HiddenInput, CharField


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


class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = ['user','phone']
        widgets = {
            'user': HiddenInput(attrs={
                'placeholder': 'user'
            }),
            'phone': TextInput(attrs={
                'placeholder': 'Номер телефону'
            }),
        }


