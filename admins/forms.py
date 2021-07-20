from products.models import Product, ProductCategory
from django.forms import fields
from users.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.forms import UserRegistrationForm, UserProfileForm


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class ProductPropertyForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.RadioSelect(attrs={'id': 'value'}))  
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')


class ProductAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите название'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4', 'placeholder': 'Введите описание'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите цену'}))
    quantity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите количество'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.RadioSelect(attrs={'id': 'value'}))
      
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')