import json
import random
import re

from check import check_match
from encoder import Encoder
from listing import Listing
from product import Product

# We'll sort products by manufacturer first
man_lookup = {}

# List of common manufacturer aliases
aliases = {
    'agfaphoto': 'agfa',
    'fuji': 'fujifilm',
    'hewlett': 'hp',
    'konica': 'konica minolta',
    'sigmatek': 'sigma'
}

with open('products.txt', encoding='utf-8') as file:
    for j in file:
        product = Product(j)
        man = product.manufacturer.lower()

        # New manufacturer
        if man not in man_lookup:
            man_lookup[man] = []

        # Enter product into data store
        man_lookup[man].append(product)

with open('listings.txt', encoding='utf-8') as file:
    mcount = 0
    lcount = 0
    word_pattern = re.compile('\w+')

    for j in file:
        listing = Listing(j)
        man = listing.manufacturer.lower()

        if man not in man_lookup:
            if man in aliases:
                # First look for manufacturer aliases match
                man = aliases[man]

            else:
                # Try to find a manufacturer match, look for words in the listing title
                for match in word_pattern.finditer(listing.title):
                    match_str = match.group(0).lower()
                    if match_str in aliases:
                        man = aliases[match_str]
                        break
                    if match_str in man_lookup:
                        man = match_str
                        break

        if man in man_lookup:
            model_matches = []
            family_matches = []

            for product in man_lookup[man]:
                match = check_match(product, listing)
                if match:
                    model_matches.append(product)
                if match >= 2:
                    family_matches.append(product)

            if len(model_matches) == 1:
                mcount += 1
                model_matches[0].matches.append(listing)

            elif len(family_matches) == 1:
                mcount += 1
                family_matches[0].matches.append(listing)

        lcount += 1
        if lcount % 1000 == 0:
            print(lcount)

print(lcount, "listings read,", mcount, "matches found")

with open('matches.txt', mode='w', encoding='utf-8') as file:
    for man in man_lookup:
        for product in man_lookup[man]:
            if len(product.matches):
                file.write(json.dumps(product, cls=Encoder, ensure_ascii=False))
                file.write('\n')
