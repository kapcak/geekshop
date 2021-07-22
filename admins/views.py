from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Админ-Панель - Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_users')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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
