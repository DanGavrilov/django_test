from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm, InformationForm
from .models import Post, Information


class Button:
    def __init__(self, text, link):
        self.text = text
        self.link = link


def register(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Авторизація', 'login'), Button('Про нас', 'about')]
    form = UserCreationForm
    in_form = InformationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.all().order_by('-date_joined').first()
            Information.objects.create(user=user, phone=request.POST['phone'])
            return redirect('login')

    data = {
        'form': form,
        'in_form': in_form,
        'buttons': buttons

    }
    return render(request, 'users/register.html', data)


def log_in(request):
    buttons = [Button('Головна сторінка', 'main'), Button('Реєстрація', 'register'), Button('Про нас', 'about')]
    form = AuthenticationForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
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
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('profile')

    data = {
        'form': form,
        'buttons': buttons
    }
    return render(request, 'users/create_post.html', data)


@login_required
def profile(request):
    posts = Post.objects.all().filter(name=request.user).order_by('-date')
    buttons = [Button('Головна сторінка', 'main'), Button('Про нас', 'about'), Button('Створити пост', 'create_post'),
               Button('Вийти', 'logout')]
    data = {
        'buttons': buttons,
        'posts': posts
    }
    return render(request, 'users/profile.html', data)

