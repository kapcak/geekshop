from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.models import User
from admins.forms import UserAdminRegistrationForm

# Create your views here.


def index(request):
    context = {'title': 'Админ-Панель'}
    return render(request, 'admins/index.html', context)


def admin_users(request):
    context = {'title': 'Админ-Панель - Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'Админ-Панель - Создание Пользователя',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update_delete(request):
    return render(request, 'admins/admin-users-update-delete.html')
