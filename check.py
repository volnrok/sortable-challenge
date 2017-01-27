from product import Product
from listing import Listing
import re

def is_match(product, listing):
    """Check if product and listing match (Assuming manufacturer already matches)"""

    # Super naive for now
    return re.search(product.model, listing.title, re.IGNORECASE)
