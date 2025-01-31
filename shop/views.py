from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product
from .forms import ProductForm

# Create your views here.

def get_product_list(request, category_slug=None):
    '''функция вытаскивает продукты и если слаг приходит заполненым то фильтрует по слагу и в конце возвращаем контексты'''
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'products': products,
        'categories': categories,
        'category': category
    }
    return render(request, 'product/product_list.html', context=context)

def get_product_detail(request, product_slug):
    '''Детализация продукта'''
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'product/product_detail.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # product.objects.create(**form.cleaned_data)
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm()
    return render(request, 'product/create_product.html', {'product_form': form})

def delete_product(request, product_slug):
    Product.objects.get(slug=product_slug).delete()
    return redirect('/')