import json
import re

class Product(object):
    """Product objects are deserialized from products JSON file"""

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.matches = []

        # Construct regex pattern for finding model
        pattern = '(^|\W)'
        first = True

        for c in self.model:
            if c.isalnum():
                if not first:
                    pattern += '[-_\s]*'
                first = False
                pattern += c

        pattern += '($|\W)'
        self.pattern = pattern
        self.pattern_c = re.compile(pattern, re.IGNORECASE)
