
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Product
from cart.forms import CartAddProductForm


def pages_num(request):
    return render(request, 'shop/product/list.html', context=context)


# page with products
def ProductList(request, category_slug=None):

    products_all = Product.objects.all()
    #создание списка
    category = None
    categories = Category.objects.all()
    #products_all = Product.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
            'category': category,
            'categories': categories,
            'products': products,
    }

    return render(request, 'shop/product/list.html/', context=context)


#products page
def ProductDetail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html/', 
        {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form,
        })

