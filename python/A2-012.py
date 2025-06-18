idk = list(map(int, input().split()))
prices = []
error = False

if len(idk) > 3:
    error = True

if error:
    print('error')
else:
    for i in range(len(idk)):
        if i == 0:
            prices.append(idk[i] * 10)
        elif i == 1:
            prices.append(idk[i] *  25)
        elif i == 2:
            prices.append(idk[i] * 3)

print(sum(prices))
