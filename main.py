from product import Product
from listing import Listing
from check import is_match

# We'll sort products by manufacturer first
man_lookup = {}

with open('products.txt') as file:
    for json in file:
        product = Product(json)
        man = product.manufacturer.lower()

        # New manufacturer
        if man not in man_lookup:
            man_lookup[man] = []

        # Enter product into data store
        man_lookup[man].append(product)

# Python has issues opening the original file, so listings 2 is the file converted to ANSI
with open('listings2.txt') as file:
    mcount = 0
    lcount = 0
    for json in file:
        listing = Listing(json)
        man = listing.manufacturer.lower()

        if man not in man_lookup:
            # Try to find a manufacturer match, do nothing for now
            pass

        if man in man_lookup:
            matches = []
            for product in man_lookup[man]:
                if is_match(product, listing):
                    matches.append(product)

            if len(matches) == 1:
                #print("Match found: ", matches[0].manufacturer, matches[0].model, listing.title)
                mcount += 1
                
        lcount += 1
        if lcount % 1000 == 0:
            print(lcount)

print(lcount, "listings read,", mcount, "matches found")

#for man in man_lookup:
    #for product in man:
        
