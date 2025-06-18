idk = input().strip().lower()
vowels = 0

for i in idk:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels += 1

print(vowels)
