n = int(input())
lines = []
line_lengths = []

for i in range(1, n + 1):
    line = [x for x in range(i)]
    lines.append(line)

for j in lines:
    line_lengths.append(len(j))

    for k in j:
        if j[k] == 0 or j[k] == len(j) - 1:
            j[k] = 0
        else:
            j[k] = 1

for a in range(len(lines[len(lines) - 1])):
    lines[len(lines) - 1][a] = 0

for _ in lines:
    print(*_)
