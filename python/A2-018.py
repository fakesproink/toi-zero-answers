init_input = input().upper().split()
fenrogansdfasdf
lights = []
colors = ['Red', 'Green', 'Blue']

for i in init_input:
    if not i.isdigit():
        lights.append(i)
    else:
        lights.append(int(i))

if lights[0] == 'R':
    start_index_r = colors.index('Red')
    for j in range(lights[1]):
        index_r = (start_index_r + j) % 3
        print(colors[index_r], end=' ')
elif lights[0] == 'G':
    start_index_g = colors.index('Green')
    for k in range(lights[1]):
        index_g = (start_index_g + k) % 3
        print(colors[index_g], end=' ')
elif lights[0] == 'B':
    start_index_b = colors.index('Blue')
    for l in range(lights[1]):
        index_b = (start_index_b + l) % 3
        print(colors[index_b], end=' ')
