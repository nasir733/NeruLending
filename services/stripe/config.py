import getdinerotoday.settings.development as development
import getdinerotoday.settings.production as production

STRIPE_CONFIG = {
    "STRIPE_PUBLISHABLE_KEY_TEST": development.STRIPE_PUBLISHABLE_KEY,
    "STRIPE_SECRET_KEY_TEST": development.STRIPE_SECRET_KEY,
    "STRIPE_PUBLISHABLE_KEY_PROD": production.STRIPE_PUBLISHABLE_KEY,
    "STRIPE_SECRET_KEY_PROD": production.STRIPE_SECRET_KEY
}


def run_production(stripe):
    if stripe:
        print("Stripe is set to PRODUCTION")
        stripe.api_key = STRIPE_CONFIG.get('STRIPE_SECRET_KEY_PROD')


def run_development(stripe):
    if stripe:
        print("Stripe is set to DEVELOPMENT")
        stripe.api_key = STRIPE_CONFIG.get('STRIPE_SECRET_KEY_TEST')
