from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.conf import settings
from ..models import *

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_common_context(request, context=None):
    if not context:
        context = {}
    context["stripe_key"] = settings.STRIPE_PUBLISHABLE_KEY
    return context


class StripeCheckout(View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        stripe_id = profile.stripe_id
        add_new_payment_method = True
        def_card = {
            'card_brand': '',
            'card_last4': ''
        }
        if stripe_id:
            stripe_user = stripe.Customer.retrieve(stripe_id)
            if stripe_user['default_source']:
                add_new_payment_method = False
                card_id = stripe_user['default_source']
                for i in stripe_user['sources']['data']:
                    if i['id'] == card_id:
                        def_card['card_brand'] = i['brand']
                        def_card['card_last4'] = i['last4']
                        break

        amount = request.session.get('ordering_price')
        products = request.session.get('ordering_products')
        return render(request,
                      "checkout/stripeCheckout.html",
                      context=get_common_context(request,
                                                 {
                                                     "add_card": add_new_payment_method,
                                                     "def_card": def_card,
                                                     "amount": amount,
                                                     "products": products
                                                 }))


def subscription(request):
    if request.method == 'POST':
        data = request.POST
        profile = Profile.objects.get(user=request.user)
        stripe_id = profile.stripe_id
        if not stripe_id:
            stripe_user = stripe.Customer.create(
                source=data['stripeToken'],
                name=f"{request.user.first_name} {request.user.last_name}",
                email=request.user.email,
            )
            profile.stripe_id = stripe_user['id']
            profile.save()
            stripe_id = stripe_user['id']
        else:
            stripe_user = stripe.Customer.retrieve(stripe_id)
            if not stripe_user['default_source']:
                stripe.Customer.modify(stripe_id, source=data['stripeToken'])
        items_month = []
        items_year = []
        for i in request.session['ordering_products']:
            if i['object']['recurring'] and i['object']['recurring']['interval'] == 'year':
                items_year.append({
                    'price': i['price'],
                    'quantity': i['quantity']
                })
            if i['object']['recurring'] and i['object']['recurring']['interval'] == 'month':
                items_month.append({
                    'price': i['price'],
                    'quantity': i['quantity']
                })
        if len(items_month) > 0:
            stripe.Subscription.create(
                customer=stripe_id,
                items=items_month
            )
        if len(items_year) > 0:
            stripe.Subscription.create(
                customer=stripe_id,
                items=items_year
            )
        amount = request.session.get('ordering_price')
        return render(request, 'userData/checkout.html', {'amount': amount})
