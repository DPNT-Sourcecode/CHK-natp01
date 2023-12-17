

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #assumre for now that SKUs are given in the format of capital letters seperated by spaces "A A B B B C"

    for char in skus:
        if char < 'A' or char > 'Z':
            return -1
        
        


