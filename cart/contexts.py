from django.shortcuts import get_object_or_404
from features.models import Post as FeatureVoted


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    
    cart = request.session.get('cart', {})
    #all added items
    cart_items = []
    #cost of all items
    total_cost = 0 
    product_count = 0
    
    for id, money_amount in cart.items():
        feature_voted = get_object_or_404(FeatureVoted, pk=id)
        total_cost += int(money_amount)
        cart_items.append({'id': id, 'money_amount': money_amount, 'feature_voted': feature_voted})
        product_count = len(cart_items)
        print(product_count)
    
    return {'cart_items': cart_items, 'product_count': product_count, 'total_cost': total_cost}