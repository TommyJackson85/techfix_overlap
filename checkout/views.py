from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import FeaturePost as FeatureVoted
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    try:
        if request.method=="POST":
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)
            
            
            if order_form.is_valid() and payment_form.is_valid():
                order = order_form.save(commit=False)
                order.date = timezone.now()
                order.save()
            
                cart = request.session.get('cart', {})
                total_cost = 0
            
                for id, money_amount in cart.items():
                    feature_voted = get_object_or_404(FeatureVoted, pk=id)
                    total_cost += int(money_amount)
                    order_line_item = OrderLineItem(
                        order=order,
                        feature_voted=feature_voted,
                        money_amount=money_amount
                    )
                    order_line_item.save()
                            
                    feature_voted.votes_cost += int(money_amount)
                            
                    remainder_euro = int(feature_voted.votes_cost)%10
                    euro_for_votes = feature_voted.votes_cost - remainder_euro
                    total_votes = int(euro_for_votes)/10 
            
                    feature_voted.votes = total_votes
                    feature_voted.save()
                        
                
     
                    customer = stripe.Charge.create(
                        amount=total_cost * 100,
                        currency="EUR",
                        description=request.user.email,
                        card=payment_form.cleaned_data['stripe_id']
                    )
                        
                if customer.paid:
                    messages.success(request, "You have successfully paid for feature request votes!")
                    request.session['cart'] = {}
                    return redirect(reverse('get_feature_posts'))
                else:
                    messages.error(request, "Unable to take payment")
            else:
                messages.error(request, "We were unable to take a payment with that card!")
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()
    except stripe.error.CardError:
        print("error occured")
        messages.error(request, "Your card was declined!")
        #return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
            
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})



    """
    except Exception as e:
        print("e:")
        print(e)
        messages.error(request, "Something wrong with your payment details")
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
    """