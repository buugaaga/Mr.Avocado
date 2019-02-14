
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Product


def pages_num(request):
    return render(request, 'shop/product/list.html', context=context)


# page with products
def ProductList(request, category_slug=None):

#нумерация страниц
    products_all = Product.objects.all()
    paginator = Paginator(products_all, 9)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

#создание списка
    category = None
    categories = Category.objects.all()
    #products_all = Product.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'category': category,
        'categories': categories,
        'products': page
    }


    return render(request, 'shop/product/list.html/', context=context)


#products page
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html/', {'product': product})
