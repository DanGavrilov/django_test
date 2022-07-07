from django.shortcuts import render
from django.http import HttpResponse



class Button:
    def __init__(self, text, link):
        self.text = text
        self.link = link


def index(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Авторизація','login'), Button('Про нас', 'about')]
    return render(request, 'main/index.html', {'buttons':buttons})


def about(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Авторизація', 'login'), Button('Про нас', 'about')]
    return render(request, 'main/about.html', {'buttons':buttons})