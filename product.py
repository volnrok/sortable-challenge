import json

class Product(object):
    """Product objects are deserialized from products JSON file"""

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.matches = []
