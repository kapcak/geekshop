from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, ProductCategory

# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'products/index.html', context=context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update({
            'title': 'geekshop - продукты',
            'categories': ProductCategory.objects.all()
        })
        return context


class ProductCategoryView(ProductListView):

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(category_id=self.kwargs['category_id'])
