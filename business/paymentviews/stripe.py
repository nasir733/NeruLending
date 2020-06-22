from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.conf import settings
from ..models import *
from user.models import UserSteps

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
        amount = 0
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

        products = request.session.get('ordering_products')
        if products:
            amount = sum([i['price_amount'] for i in products])
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

        # Create new stripe customer or add payment method to existing customer.
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

        # Generate new subscriptions to products from session['ordering_products']
        products = request.session.get('ordering_products')
        items = {
            'year': [],
            'month': []
        }
        for i in products:
            for key in items:
                if i['object']['recurring'] and i['object']['recurring']['interval'] == key:
                    items[key].append({
                        'price': i['price'],
                        'quantity': i['quantity']
                    })
        for i, k in items.items():
            if len(k) > 0:
                stripe.Subscription.create(
                    customer=stripe_id,
                    items=k
                )

        # Add UserSteps if there is in session
        user_steps_data = request.session.get('user_steps_data')
        if user_steps_data:
            new_steps = UserSteps(
                **user_steps_data
            )
            new_steps.save()
            request.session.pop('user_steps_data')

        amount = sum([i['price_amount'] for i in products])
        request.session.pop('ordering_products')
        return render(request, 'checkout/checkout.html', {'amount': amount})


def remove(request):
    if request.method == 'POST':
        data = request.POST
        if 'delete_item' in data and data['delete_item']:
            items = request.session.get('ordering_products')
            for i in items.copy():
                if i['price'] == data['delete_item']:
                    items.remove(i)
            request.session['ordering_products'] = items
        return redirect("business:stripe_checkout")


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=request.POST['amount'],
            currency='usd',
            description='Get Dinero Today Service Charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'checkout/checkout.html', {'amount': request.POST['amount']})
