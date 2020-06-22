import stripe
import payments.stripe.config as config
config.run_production(stripe)


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