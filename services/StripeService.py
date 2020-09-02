import stripe

from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeService:

    @staticmethod
    def create_user(**kwargs):
        stripe_user = stripe.Customer.create(
            name=f"{kwargs['first_name']} {kwargs['last_name']}",
            email=kwargs['email']
        )
        return stripe_user
