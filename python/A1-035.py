n = int(input())
base = 1
result = 0

for i in range(n):
    result += pow(base, 2)
    base += 1

print(result)
