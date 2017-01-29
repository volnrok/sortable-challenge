from product import Product
from listing import Listing
import re

def is_match(product, listing):
    """Check if product and listing match (Assuming manufacturer already matches)"""

    # Use regex created in product initialization
    c_found = bool(product.pattern_c.search(listing.title))
    #m_found = re.search(product.model, listing.title, re.IGNORECASE)

    #if c_found != m_found:
        #print(c_found, p_found, product.manufacturer, product.model, listing.title, sep=', ')

    return c_found
