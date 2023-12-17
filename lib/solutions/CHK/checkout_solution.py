

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #assumre for now that SKUs are given in the format of capital letters seperated by NO spaces "AABBC"
    prices = {
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15,
        "E" : 40,
        "F" : 10,
        "G" : 20,
        "H" : 10,
        "I" : 35,
        "J" : 60,
        "K" : 70,
        "L" : 90,
        "M" : 15,
        "N" : 40,
        "O" : 10,
        "P" : 50,
        "Q" : 30,
        "R" : 50,
        "S" : 20,
        "T" : 20,
        "U" : 40,
        "V" : 50,
        "W" : 20,
        "X" : 17,
        "Y" : 20,
        "Z" : 21
    }

    #offers are stored in list of tuples where each tuple represents a possible offer, with the offer that is most beneficial for the customer being first

    # (A,B) quantity A for B money
    special_offers_money = {
        "A" : [(5,200),(3,130)],
        "B":[(2,45)],
        "F":[(3,20)],
        "H":[(10,80),(5,45)],
        "K":[(2,120)],
        "P":[(5,200)],
        "Q":[(3,80)],
        "U":[(4,120)],
        "V":[(3,130),(2,90)]
    }

    # (A,B) quantity A get a B free
    special_offers_items = {
        "E":[(2,"B")],
        "N":[(3,"M")],
        "R":[(3,"Q")],
    }

    #list of items in the group offer begining with the most expensive to benefit the user
    group_offer_items = ["Z","S","T","Y","X"]
    
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

    #Free item discount
    #(for now this works only when the free items are not items that at a certain quantity have free items too since that can give inaccurate results)
    for item in special_offers_items:
        if item in contents:
            num_of_item = contents[item]
            item_being_free = special_offers_items[item][0][1]
            num_to_trigger_offer = special_offers_items[item][0][0]
            total+= prices[item]*num_of_item
            item_free_remove_quantity = num_of_item // num_to_trigger_offer

            if item_being_free in contents:
                contents[item_being_free] = contents[item_being_free] - item_free_remove_quantity if contents[item_being_free] > item_free_remove_quantity else  0

            contents[item] = 0

    #Group offers
    # this are defined before the execution of the code so that if more group offers come in the future we can include the whole section in a loop with different values for the offer
    group_offer_count = 0
    group_offer_price = 45
    group_offer_quant = 3

    for item in group_offer_items:
        if item in contents:
            num_of_item = contents[item]

            group_offer_count += num_of_item
            total += group_offer_price * (group_offer_count // group_offer_quant)
            group_offer_count -= (group_offer_count // group_offer_quant) * group_offer_quant

    #put the remaining quantity of items that were present in the group offer and the basket to the cheapest possible items
    items_remain = group_offer_count
    for item in group_offer_items[::-1]:
        if item in contents:
            if items_remain == 0:
                contents[item] = 0
            elif items_remain <= contents[item]:
                contents[item] = items_remain
                items_remain = 0
            else:
                items_remain -= contents[item]

    for item in contents:
        num_of_item = contents[item]
        if num_of_item == 0:
            continue

        #Money Discount
        elif item in special_offers_money:
            for discount in special_offers_money[item]:
                total += (num_of_item // discount[0]) * discount[1]
                num_of_item -= discount[0] * (num_of_item // discount[0])

            total += prices[item] * num_of_item

        #No discount
        else:
            total += prices[item] * num_of_item

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

def test_f():
    skus = "F" * 10

    assert checkout(skus) == 70

    skus = "AAABBBAACDBDEEEEEFFF" #5A4B1C2D5E3F

    assert checkout(skus) == 515

    skus = "AAABBBAACDBDEEEEEFFF" #5A4B1C2D5E2F

    assert checkout(skus) == 515

def test_random_checks():
    skus = 3*"A" + 10*"H" + 3*"R" + 4*"Q"

    assert checkout(skus) == 440

def test_simple_group_offer():
    skus = "STXYZ"

    assert checkout(skus) == 82

def test_more_complex_group_offer():
    skus = "SSTXYZZZ"

    assert checkout(skus) == 127

def test_mixed_complex_group_offer():
    skus = "SSTXYZZZ" + 3*"A" + 10*"H" + 3*"R" + 4*"Q"

    assert checkout(skus) == 127 + 440