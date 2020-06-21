import stripe
from payments.stripe.config import STRIPE_CONFIG
stripe.api_key = STRIPE_CONFIG.get("STRIPE_SECRET_KEY_TEST")


def create_customer():
    return stripe.Customer.create(
        description="My First Test Customer (created for API docs)",
    )


def lsit_customers():
    return stripe.Customer.list(limit=3)

a = stripe.Customer.list(limit=2)['data'][1]

a['default_source']

def list_products():
    stripe.Product.list()

def list_prices():
    a = stripe.Price.list()