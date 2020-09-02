import stripe

from payments.stripe.config import STRIPE_CONFIG
from payments.stripe.product_list import products

stripe.api_key = STRIPE_CONFIG.get("STRIPE_SECRET_KEY_PROD")


def create_product(product):
    # Get product id if exists or create new product and get its id if not.
    product_list = stripe.Product.list()['data']
    for i in product_list:
        if i.name == product['name']:
            print(f"Product {i.name} already exists")
            product_id = i.id
            break
    else:
        new_product = stripe.Product.create(name=product['name'])
        product_id = new_product.id
        print(f"Created product {product['name']}")

    prices = stripe.Price.list(product=product_id)['data']

    if len(prices) > 0:
        for price in prices:
            if price["recurring"]["interval"] == "month" and int(product["price_monthly"] * 100) != price[
                "unit_amount"]:
                stripe.Price.create(
                    unit_amount=int(product['price_monthly'] * 100),
                    currency="usd",
                    recurring={"interval": "month"},
                    product=product_id,
                    lookup_key=f"{product['name']}_monthly",
                    transfer_lookup_key=True,
                )
                print(f"Updated monthly price for {product['name']} : {product['price_monthly']}")
            elif price["recurring"]["interval"] == "year" and int(product["price_yearly"] * 100) != price[
                "unit_amount"]:
                stripe.Price.create(
                    unit_amount=int(product['price_yearly'] * 100),
                    currency="usd",
                    recurring={"interval": "year"},
                    product=product_id,
                    lookup_key=f"{product['name']}_yearly",
                    transfer_lookup_key=True,
                )
                print(f"Updated yearly price for {product['name']} : {product['price_yearly']}")

    else:
        if product['price_monthly']:
            stripe.Price.create(
                unit_amount=int(product['price_monthly'] * 100),
                currency="usd",
                recurring={"interval": "month"},
                product=product_id,
                lookup_key=f"{product['name']}_monthly"
            )
            print(f"Created new monthly price for {product['name']} : {product['price_monthly']}")

        if product['price_yearly']:
            stripe.Price.create(
                unit_amount=int(product['price_yearly'] * 100),
                currency="usd",
                recurring={"interval": "year"},
                product=product_id,
                lookup_key=f"{product['name']}_yearly"

            )
            print(f"Created new yearly price for {product['name']} : {product['price_yearly']}")


def generate_products(prods):
    for i in prods:
        create_product(i)


generate_products(products)
