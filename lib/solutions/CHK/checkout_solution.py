

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #assumre for now that SKUs are given in the format of capital letters seperated by spaces "A A B B B C"
    contents = {}

    for char in skus.split():
        if char < 'A' or char > 'Z':
            return -1
        
        contents[char] = contents.get(char, 0) + 1

    total = 0

    for item in contents:
        if item == 'A':
            total += 


