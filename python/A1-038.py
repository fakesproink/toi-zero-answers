n = int(input().strip())

for i in range(n):
    if (i + 1) % 5 == 0 and i != 0:
        print('X', end='')
    else:
        print('*', end='')
