import json

class Listing(object):
    """Listing objects are deserialized from listings JSON file"""

    def __init__(self, j):
        self.__dict__ = json.loads(j)
