food = []
item_count = [0, 0, 0, 0]
calories = 0
calorie_per_item = [100, 120, 200, 60]

while True:
    idk = int(input().strip())
    food.append(idk)

    if 5 in food:
        print("Bye Bye")
        break

for i in food:
    if i == 1:
        item_count[0] += 1
    elif i == 2:
        item_count[1] += 1
    elif i == 3:
        item_count[2] += 1
    elif i == 4:
        item_count[3] += 1
    else:
        pass

for j in range(4):
    calories += item_count[j] * calorie_per_item[j]

print('Total Calories: ' + str(calories))
