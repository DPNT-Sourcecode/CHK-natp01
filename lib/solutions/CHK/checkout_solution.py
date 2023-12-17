

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #assumre for now that SKUs are given in the format of capital letters seperated by NO spaces "AABBC"
    contents = {}

    if not skus:
        return 0

    if not isinstance(skus, str):
        return -1
    
    for el in skus:
        if el < 'A' or el > 'Z':
            return -1
        
        contents[el] = contents.get(el, 0) + 1

    total = 0

    for item in contents:
        num = contents[item]
        if item == 'A':
            total += (num // 3) * 130 + (num % 3) * 50
        elif item == 'B':
            total += (num // 2) * 45 + (num % 2) * 30
        elif item == 'C':
            total+= 20*num
        elif item == 'D':
            total+= 15*num

    return total

def test_checkout():
    skus = ""
    assert checkout(skus) == -1

    skus="a"
    assert checkout(skus) == -1
    skus="1"
    assert checkout(skus) == -1
    skus=1
    assert checkout(skus) == -1

    skus = []
    skus = "A"
    assert checkout(skus) == 50

    skus += "B"
    assert checkout(skus) == 80

    skus += "CD"
    assert checkout(skus) == 115

    skus += "AA"
    assert checkout(skus) == 195

    skus += "BB"
    assert checkout(skus) == 240

