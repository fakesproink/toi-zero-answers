n = int(input())
inputs = []
vowel_count = 0

for i in range(n):
    letter_input = input().strip().upper()
    inputs.append(letter_input)

for j in inputs:
    if j == "A" or j == "E" or j == "I" or j == "O" or j == "U":
        vowel_count += 1

print(vowel_count)
