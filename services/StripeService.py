import stripe

from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeService:

    @staticmethod
    def create_user(**kwargs):
        stripe_user = stripe.Customer.create(
            name=f"{kwargs.get('first_name')} {kwargs.get('last_name')}",
            email=kwargs.get('email'),
            source=kwargs.get('source')
        )
        return stripe_user

    @staticmethod
    def add_source_to_user(customer_id, source):
        stripe.Customer.modify(customer_id, source=source)

    @staticmethod
    def get_user_by_id(customer_id):
        return stripe.Customer.retrieve(customer_id)

    @staticmethod
    def new_product(name):
        new_product = stripe.Product.create(name=name)
        return new_product

    @staticmethod
    def get_product(product_id):
        product = stripe.Product.retrieve(product_id)
        return product

    @staticmethod
    def get_product_by_name(name):
        product_list = stripe.Product.list()['data']
        for i in product_list:
            if i.name == name:
                return i

    @staticmethod
    def has_product_id(product_id):
        if StripeService.get_product(product_id):
            return True
        return False

    @staticmethod
    def get_product_prices(product_id):
        return stripe.Price.list(product=product_id)['data']

    @staticmethod
    def save_product(product):
        prices = StripeService.get_product_prices(product['id'])

    @staticmethod
    def charge_card(source, amount, description):
        stripe.Charge.create(
            amount=amount,
            currency='usd',
            description=description,
            source=source
        )

    @staticmethod
    def charge_customer(customer_id, amount, description):
        stripe.Charge.create(
            amount=amount,
            currency='usd',
            description=description,
            customer=customer_id
        )

    @staticmethod
    def create_price(price, lookup_key, product_id, recurring=None):
        new_price = stripe.Price.create(
            unit_amount=price,
            currency="usd",
            product=product_id,
            recurring=recurring,
            lookup_key=lookup_key,
            transfer_lookup_key=True
        )
        return new_price

    @staticmethod
    def delete_product(product_id):
        product = StripeService.get_product(product_id)
        stripe.Product.modify(product_id, active=False, name=f"deleted_{product.name}")

    @staticmethod
    def _get_recurring_rule(name, recurring):
        if recurring == 1:
            lookup_key = f"{name}_one_time"
            recurring_rule = None
        elif recurring == 2:
            lookup_key = f"{name}_monthly"
            recurring_rule = {"interval": "month"}
        elif recurring == 3:
            lookup_key = f"{name}_yearly"
            recurring_rule = {"interval": "year"}
        else:
            raise Exception("Wrong recurring rule, must be: 1 (one time) / 2 (monthly) / 3 (yearly)")
        return lookup_key, recurring_rule

    @staticmethod
    def _det_recurring_rule_from_stripe(price):
        if price.type == "one_time":
            return 1
        elif price.type == "recurring" and price.recurring.interval == "month":
            return 2
        elif price.type == "recurring" and price.recurring.interval == "year":
            return 3

    @staticmethod
    def create_product(name, price, description=None, recurring=1):
        price = int(price * 100)
        new_product = StripeService.new_product(name)
        lookup_key, recurring_rule = StripeService._get_recurring_rule(name, recurring)
        new_price = StripeService.create_price(price, lookup_key, new_product.id, recurring_rule)
        return {
            "prod_id": new_product.id,
            "price_id": new_price.id,
            "price_lookup": lookup_key
        }

    @staticmethod
    def update_product(product_id, price_id, name, new_price, recurring=1):
        new_price = int(new_price * 100)
        product = StripeService.get_product(product_id)
        if product.name != name:
            stripe.Product.modify(product_id, name=name)
        price = stripe.Price.retrieve(price_id)
        lookup_key, recurring_rule = StripeService._get_recurring_rule(name, recurring)
        if price.unit_amount != new_price or recurring != StripeService._det_recurring_rule_from_stripe(price):
            new_price_obj = StripeService.create_price(new_price, lookup_key, product_id, recurring_rule)
            stripe.Price.modify(price_id, active=False)
            price_id = new_price_obj.id
        return price_id, lookup_key

    @staticmethod
    def get_price(price_id):
        return stripe.Price.retrieve(price_id)

    @staticmethod
    def create_subscription(**kwargs):
        stripe.Subscription.create(**kwargs)

    @staticmethod
    def make_purchases(products, customer_id, source_id=None):
        recurring_items = {
            "year": [],
            "month": [],
        }
        one_time = {
            'total': 0,
            'name': ''
        }

        for product in products:
            stripe_price = StripeService.get_price(product['price_id'])
            if stripe_price.type == 'recurring':
                item = {'price': stripe_price.id, 'quantity': product['quantity']}
                if stripe_price.recurring.interval == 'year':
                    recurring_items['year'].append(item)
                elif stripe_price.recurring.interval == 'month':
                    recurring_items['month'].append(item)
            elif stripe_price.type == 'one_time':
                one_time['total'] += stripe_price.unit_amount * product['quantity']
                one_time['name'] += product['name'] + ", "

        for interval, items in recurring_items.items():
            if len(items) > 0:
                StripeService.create_subscription(customer=customer_id, items=items, default_source=source_id)
        if one_time['total'] > 0:
            StripeService.charge_customer(source_id if source_id else customer_id, one_time['total'], one_time['name'])
