from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Category


def cart(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(
			initial={
			'quantity': item['quantity'],
			'update': True
			})
	return({'cart': cart})

def categories(request):
	categories = Category.objects.all()
	return {'categories': categories}