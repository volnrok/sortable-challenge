import json
import re

def create_pattern(s):
    """Create a pattern for finding model or family in a listing"""

    pattern = '(^|\W)'
    first = True

    for c in s:
        if c.isalnum():
            if not first:
                pattern += '[-_\s]*'
            first = False
            pattern += c

    pattern += '($|\W)'
    return pattern

class Product(object):
    """Product objects are deserialized from products JSON file"""

    def __init__(self, j):

        self.__dict__ = json.loads(j)
        self.matches = []

        # Construct regex pattern for finding model and family
        self.model_pattern = create_pattern(self.model);
        self.model_pattern_c = re.compile(self.model_pattern, re.IGNORECASE)

        if hasattr(self, 'family'):
            self.family_pattern = create_pattern(self.family);
            self.family_pattern_c = re.compile(self.family_pattern, re.IGNORECASE)

    def default(self, o):
        return {
            'product_name': o.product_name,
            'listings': o.matches
        }
