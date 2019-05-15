from django.shortcuts import get_object_or_404
from bugs.models import Post as BugPost


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        bug_post = get_object_or_404(BugPost, pk=id)
        total += quantity * bug_post.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'bug_post': bug_post})
    
        return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}