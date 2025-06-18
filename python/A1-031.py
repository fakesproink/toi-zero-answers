idk = input().strip()
reversed_something = idk[::-1]
result = list('')

for i in range(len(reversed_something)):
    if i != 0 and i % 3 == 0:
        result.append(',')
    result.append(reversed_something[i])

print(''.join(result[::-1]))
