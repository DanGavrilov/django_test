from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.template.defaulttags import url
from .forms import UserForm
from .models import Post


class Button:
    def __init__(self, text, link):
        self.text = text
        self.link = link


def register(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Авторизація', 'login'), Button('Про нас', 'about')]
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    data = {
        'form':form,
        'buttons':buttons
    }
    return render(request, 'users/register.html', data)


def log_in(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Реєстрація', 'register'), Button('Про нас', 'about')]
    form = AuthenticationForm
    if request.method == 'POST':
        username_ = request.POST['username']
        password_ = request.POST['password']
        user = authenticate(request, username=username_, password=password_)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            print('помилка')

    return render(request, 'users/login.html', {'buttons': buttons, 'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('main')


@login_required
def create_post(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Про нас', 'about'), Button('Вийти', 'logout')]
    form = UserForm
    form.name = request.user

    if request.method == 'POST':
        print(request.user)
        form = UserForm(request.POST)
        form.name = request.user
        form.save(commit=False)
        if form.is_valid():
            form.save()
            return redirect('profile')
    data = {
        'form': form,
        'buttons': buttons
    }
    return render(request, 'users/create_post.html', data)


@login_required
def profile(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Про нас', 'about'), Button('Створити пост', 'create_post'), Button('Вийти', 'logout')]
    data = {
        'buttons':buttons
    }
    return render(request, 'users/profile.html', data)

