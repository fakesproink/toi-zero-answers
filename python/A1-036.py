n = int(input())
nums = []

if str(n)[len(str(n)) - 1] != '0':
    nums = []
else:
    nums = [n]

for i in range(n):
    n -= 1
    if n % 10 == 0:
        nums.append(n)

print(*nums)
