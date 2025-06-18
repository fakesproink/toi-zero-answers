n, m = map(int, input().split())
n_pos = list(map(int, input().split()))
m_pos = list(map(int, input().split()))
n_coords = []
m_coords = []
m_up = [i / 10 for i in range(11)]
m_down = [i / 10 for i in range(10, -1, -1)]
n_up = []
n_down = []

for i, j in zip(m_up, m_down):
    if int(str(i)[::-1][0]) % 2 == 0 or int(str(j)[::-1][0]) % 2 == 0:
        n_up.append(i)
        n_down.append(j)

print(n_coords)
