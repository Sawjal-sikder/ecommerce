from .models import shopcart
from products.models import Category

def context_card(request):
    categories = Category.objects.all()
    user = request.user
    cart = []
    cartlen = 0
    if user.is_authenticated:
        cart = shopcart.objects.filter(user=user)
        cartlen = cart.count()
    return {'cart': cart, 'cartlen': cartlen, 'categories':categories}
