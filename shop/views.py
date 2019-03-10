
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart

def pages_num(request):
    return render(request, 'shop/product/list.html', context=context)
 

# page with products
def ProductList(request, category_slug=None):

    
    #создание списка
    category = None
    categories = Category.objects.all()
    #products_all = Product.objects.all()
    products_all = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_all = products_all.filter(category=category)

    context = {
            'category': category,
            'categories': categories,
            'products_all': products_all,
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

