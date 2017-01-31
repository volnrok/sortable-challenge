from product import Product
from listing import Listing
import re

def check_match(product, listing):
    """Check if product and listing match (Assuming manufacturer already matches)"""

    # Use regex created in product initialization
    m_found = product.model_pattern_c.search(listing.title)

    if m_found:
        if hasattr(product, 'family'):
            f_found = product.family_pattern_c.search(listing.title)

            if f_found:
                # model and family match
                return 2

        # model match
        return 1

    # no match
    return 0
