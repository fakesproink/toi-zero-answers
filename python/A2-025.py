r, c = map(int, input().split())
rb, cb = map(int, input().split())
n = int(input())
infected = [tuple(map(int, input().split())) for _ in range(n)]
risk_grid = [[0 for __ in range(c)] for __ in range(r)]

for ir, ic in infected:
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            dist = abs(dr) + abs(dc)
            if dist > 2:
                continue
            nr, nc = ir + dr, ic + dc
            if 0 <= nr < r and 0 <= nc < c:
                if dist == 0:
                    risk = 100
                elif dist == 1:
                    risk = 60
                elif dist == 2:
                    risk = 20
                risk_grid[nr][nc] = max(risk_grid[nr][nc], risk)

safe_count = sum(1 for row in risk_grid for val in row if val == 0)
print(safe_count)

risk = risk_grid[rb][cb]
print(f"{risk}%")
