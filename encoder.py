import json

from product import Product
from listing import Listing

class Encoder(json.JSONEncoder):
    """Encoder for Product and Listing objects"""

    def default(self, o):
        
        if isinstance(o, Product):
            return {
                'product_name': o.product_name,
                'listings': o.matches
            }

        elif isinstance(o, Listing):
            return o.__dict__

        else:
            return json.JSONEncoder.default(self, o)
