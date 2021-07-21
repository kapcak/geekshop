from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import User
from products.models import Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductPropertyForm, ProductAddForm

# Create your views here.


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-Панель'}
    return render(request, 'admins/index.html', context)



class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {'title': 'Админ-Панель - Пользователи',
#                'users': User.objects.all()}
#     return render(request, 'admins/admin-users-read.html', context)


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_users')

# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(
#             data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {
#         'title': 'Админ-Панель - Создание Пользователя',
#         'form': form,
#     }
#     return render(request, 'admins/admin-users-create.html', context)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(
#             instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {
#         'title': 'Админ-панель - Редактирование пользователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_remove(request, pk):
#     user = User.objects.get(id=pk)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_staff)
def admin_product_read(request):
    context = {
        'title': 'Админ-панель - Продукты',
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_update(request, pk):
    selected_product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductPropertyForm(
            instance=selected_product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product_read'))
    else:
        form = ProductPropertyForm(instance=selected_product)
    context = {
        'title': 'Админ-панель - Редактирование товара',
        'form': form,
        'selected_product': selected_product,
    }
    return render(request, 'admins/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product_read'))
    else:
        form = ProductAddForm()
    context = {
        'title': 'Админ-Панель - Добавление товара',
        'form': form,
    }
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_remove(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_product_read'))
