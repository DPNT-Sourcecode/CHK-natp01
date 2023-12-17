

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #assumre for now that SKUs are given in the format of capital letters seperated by spaces "A A B B B C"
    contents = {}

    if not skus:
        return -1
    
    for char in skus.split():
        if char < 'A' or char > 'Z':
            return -1
        
        contents[char] = contents.get(char, 0) + 1

    total = 0

    for item in contents:
        num = contents[item]
        if item == 'A':
            total += (num // 3) * 130 + (num % 3) * 50
        elif item == 'B':
            total += (num // 2) * 45 + (num % 2) * 530
        elif item == 'C':
            total+= 20*num
        elif item == 'D':
            total+= 15*num

    return total

def test_checkout():
    skus = []
    assert checkout(skus) == -1

    skus.append("a")
    assert checkout(skus) == -1
    skus[0] = 1
    assert checkout(skus) == -1

    skus = []
    skus.append("A")
    assert checkout(skus) == 50

    skus.append("B")
    assert checkout(skus) == 80

    skus.extend(["C","D"])
    assert checkout(skus) == 


