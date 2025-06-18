num1 = int(input())
num2 = int(input())
num3 = int(input())
nums = [num1, num2, num3]

even_nums = 0
odd_nums = 0

for i in nums:
    if i % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print("even " + str(even_nums))
print("odd " + str(odd_nums))
