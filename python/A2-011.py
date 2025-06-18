nums = list(map(int, input().split()))
result = []

for i in nums:
    if i not in result:
        result.append(i)

print(*result)
