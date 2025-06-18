def display_card_type(idk, symbol):
    returnvalue1 = ""
    returnvalue2 = ""

    if idk == "A":
        returnvalue1 = "ace"
    elif idk == "J":
        returnvalue1 = "jack"
    elif idk == "Q":
        returnvalue1 = "queen"
    elif idk == "K":
        returnvalue1 = "king"

    if symbol == "D":
        returnvalue2 = "diamonds"
    elif symbol == "H":
        returnvalue2 = "hearts"
    elif symbol == "S":
        returnvalue2 = "spades"
    elif symbol == "C":
        returnvalue2 = "clubs"

    if idk.isdigit():
        return idk + " of " + returnvalue2
    else:
        return returnvalue1 + " of " + returnvalue2
    

card = input().strip().upper()
num = ''
chars = ''
for i in card:
    if i.isdigit():
        num += i
    elif isinstance(i, str):
        chars += i
    else:
        break

if num == '':
    print(display_card_type(chars[0], chars[1]))
else:
    print(display_card_type(num, chars))
