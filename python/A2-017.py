main_stuff = input().lower().split()
extra = input().lower().split()
toppings = []
prices = []

for i in extra:
    if not i.isdigit():
        toppings.append(i)
    else:
        toppings.append(int(i))

for j in range(len(main_stuff)):
    # small
    if main_stuff[j] == 's' and main_stuff[j + 1] == 'r':
        prices.append(60)
    elif main_stuff[j] == 's' and main_stuff[j + 1] == 't':
        prices.append(80)

    # medium
    elif main_stuff[j] == 'm' and main_stuff[j + 1] == 'r':
        prices.append(80)
    elif main_stuff[j] == 'm' and main_stuff[j + 1] == 't':
        prices.append(100)

    # large
    elif main_stuff[j] == 'l' and main_stuff[j + 1] == 'r':
        prices.append(100)
    elif main_stuff[j] == 'l' and main_stuff[j + 1] == 't':
        prices.append(120)

if len(toppings) == 1:
    print(sum(prices))
else:
    for k in range(len(toppings)):
        if toppings[k] == 'p':
            prices.append(toppings[k + 1] * 15)
        elif toppings[k] == 'e':
            prices.append(toppings[k + 1] * 10)

    print(sum(prices))
