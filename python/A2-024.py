l, p = map(int, input().split())
r, m, f = map(int, input().split())
r_score = 0
m_score = 0
f_score = 0
checkpoints = {}

for _ in range(p):
    dist, points = map(int, input().split())
    checkpoints[dist] = points

# rabbit
pos = 0
while pos <= l:
    if pos in checkpoints:
        r_score += checkpoints[pos]
    pos += r

# monkey
pos = 0
while pos <= l:
    if pos in checkpoints:
        m_score += checkpoints[pos]
    pos += m

# french mfs
pos = 0
while pos <= l:
    if pos in checkpoints:
        f_score += checkpoints[pos]
    pos += f

scores = {
    'Rabbit': r_score,
    'Monkey': m_score,
    'Frog': f_score
}

for i in ['Rabbit', 'Monkey', 'Frog']:
    if scores[i] == max(scores.values()):
        print(f"{i} {max(scores.values())}")
