

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

    if "E" in contents:
        num = contents["E"]
        total+= 40*num
        b_remove = contents["E"] // 2

        if "B" in contents:
            contents["B"] = contents["B"] - b_remove if contents["B"] > b_remove else  0

        del contents["E"]

    if "F" in contents:
        contents["F"] -= contents["F"] // 3

    for item in contents:
        num = contents[item]
        if item == 'A': # first apply 5A for 200 offer since it is a better deal for the customer
            total += (num//5) * 200
            num -= 5 * (num // 5)
            total += (num // 3) * 130 + (num % 3) * 50
        elif item == 'B':
            total += (num // 2) * 45 + (num % 2) * 30
        elif item == 'C':
            total+= 20*num
        elif item == 'D':
            total+= 15*num
        elif item == "F":

    return total

def test_checkout():
    skus = ""
    assert checkout(skus) == 0

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

    skus = "ABCa"
    assert checkout(skus) == -1

def test_new_a_offer():
    skus = "AAAAAAAA"

    assert checkout(skus) == 330

    skus = "AAAAAAAAA"

    assert checkout(skus) == 380
    
def test_e_offer():
    skus = "ABCDEE"

    assert checkout(skus) == 165

def more_complicated():
    skus = "AAABBBAACDBDEEEEE" #5A4B1C2D5E

    assert checkout(skus) == 495

