from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request): 
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first before adding feature request votes to cart! Your previous cart items have been removed.")
        return redirect('login')
    """Add a quantity of the specified product to the cart"""
    money_amount = request.POST.get('money_amount')
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, money_amount)
    request.session['cart'] = cart
    return redirect(view_cart)


def adjust_cart(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first before adjust cart items! Your previous cart items have been removed.")
        return redirect('login')
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    cart = request.session.get('cart', {})
    quantity_string = request.POST.get('quantity')
    if quantity_string is '':
        cart.pop(id)
    else:
        quantity = int(quantity_string)
        if quantity > 0:
            cart[id] = quantity
        else:
            cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))