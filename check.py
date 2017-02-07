from product import Product
from listing import Listing
import re

def check_match(product, listing):
    """Check if product and listing match (Assuming manufacturer already matches)"""

    # Use regex created in product initialization
    m_found = product.model_pattern_c.search(listing.title)

    # Store the results in a dictionary
    result = {
        'm_match': False, # Model matches
        'f_match': False, # Model and family match
        'm_index': -1 # Start index of model match
    }

    if m_found:
        result['m_match'] = True
        result['m_index'] = m_found.start(0)

        if hasattr(product, 'family'):
            f_found = product.family_pattern_c.search(listing.title)
            result['f_match'] = bool(f_found)

    return result
