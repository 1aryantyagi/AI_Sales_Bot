import json
import stripe
from fuzzywuzzy import process
from langchain.agents import tool

# Load Product Catalog
with open("product_catalog.json", "r") as file:
    PRODUCT_CATALOG = json.load(file)


@tool
def get_product_info(search_term: str) -> dict:
    """Retrieve product details by product ID, name, or category."""
    # Try direct ID match first
    for product in PRODUCT_CATALOG:
        if product["id"] == search_term:
            return product

    # Fuzzy search by name or category
    product_names = [product["name"] for product in PRODUCT_CATALOG]
    best_match, score = process.extractOne(search_term, product_names)
    if score > 70:  # Threshold for similarity
        for product in PRODUCT_CATALOG:
            if product["name"] == best_match:
                return product

    return {"error": "Product not found"}


@tool
def generate_stripe_payment_link(product_id: str, customer_email: str) -> str:
    """Generate Stripe payment link for a product."""
    product = get_product_info(product_id)
    if "error" in product:
        return product["error"]

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': product['stripe_price_id'],
                'quantity': 1,
            }],
            mode='payment',
            customer_email=customer_email,
            success_url='https://yourdomain.com/success',
            cancel_url='https://yourdomain.com/cancel',
        )
        return session.url
    except Exception as e:
        return f"Error creating payment link: {str(e)}"


@tool
def check_mindware_compatibility(customer_industry: str) -> str:
    """Check solution compatibility with customer's industry through Mindware."""
    compatible_industries = ["technology",
                             "finance", "healthcare", "education"]
    return "Compatible" if customer_industry.lower() in compatible_industries else "Not Compatible"
