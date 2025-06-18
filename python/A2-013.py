idk = list(input().split())
tea = list(input().split())
idk_cleaned = []
tea_cleaned = []
calories = []

for i in idk:
    if not i.isdigit():
        idk_cleaned.append(i.upper())
    else:
        idk_cleaned.append(int(i))

for j in tea:
    if not j.isdigit():
        tea_cleaned.append(j.upper())
    else:
        tea_cleaned.append(int(j))

# boba calories
if 'H' in idk_cleaned:
    calories.append(idk_cleaned[1] * 5)
elif 'O' in idk_cleaned:
    calories.append(idk_cleaned[1] * 3)
elif 'J' in idk_cleaned:
    calories.append(idk_cleaned[1] * 2)

# tea calories
if 'R' in tea_cleaned:
    if tea_cleaned[1] == 1:
        calories.append(tea_cleaned[2] * 12)
    elif tea_cleaned[1] == 2:
        calories.append(tea_cleaned[2] * 18)
    elif tea_cleaned[1] == 3:
        calories.append(tea_cleaned[2] * 25)

elif 'T' in tea_cleaned:
    if tea_cleaned[1] == 1:
        calories.append(tea_cleaned[2] * 15)
    elif tea_cleaned[1] == 2:
        calories.append(tea_cleaned[2] * 20)
    elif tea_cleaned[1] == 3:
        calories.append(tea_cleaned[2] * 30)

elif 'M' in tea_cleaned:
    if tea_cleaned[1] == 1:
        calories.append(tea_cleaned[2] * 10)
    elif tea_cleaned[1] == 2:
        calories.append(tea_cleaned[2] * 15)
    elif tea_cleaned[1] == 3:
        calories.append(tea_cleaned[2] * 20) 

print(sum(calories))
