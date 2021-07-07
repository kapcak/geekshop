from django.shortcuts import render
from users.forms import UserLoginForm


# Create your views here.

def login(request):
    context = {
        'title': 'GeekShop - Авторизация',
        'form': UserLoginForm,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    return render(request, 'users/registration.html')
