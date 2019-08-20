from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    print(request.POST.get('money_amount'))
    money_amount = request.POST.get('money_amount')
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, money_amount)
    
    print("checking money_amount")
    print(cart)
    print([id])

    request.session['cart'] = cart
    return redirect(view_cart)


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    print(request)
    print(request.POST.get('quantity'))
    print('its string')
    
    quantity = int(request.POST.get('quantity'))
        
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
        print("checking quantity")
        print(cart)
        print([id])
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('view_cart'))