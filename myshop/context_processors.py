from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Category


def context_processor(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(
			initial={
			'quantity': item['quantity'],
			'update': True
			})

	categories = Category.objects.all()

	return {'cart': cart,'categories': categories}
