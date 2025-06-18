n, m = map(int, input().split())
k = int(input())
grid = [[0 for __ in range(m)] for a in range(n)]
p_coords = []
available_spots = []
directions = [(-1, -1), (-1, 0), (-1, +1),
              ( 0, -1),          ( 0, +1),
              (+1, -1), (+1, 0), (+1, +1)]

for _ in range(k):
    p = list(map(int, input().split()))
    p_coords.append(p)

for r, c in p_coords:
    grid[r][c] += 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            spot = [i, j]
            available_spots.append(spot)

max_catch = 0
for i, j in available_spots:
    count = 0
    for dr, dc in directions:
        nr, nc = i + dr, j + dc
        if 0 <= nr < n and 0 <= nc < m:
            count += grid[nr][nc]
    max_catch = max(max_catch, count)

print(max_catch)
