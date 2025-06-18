N, M = map(int, input().split())
events = []

for _ in range(M):
    s, t = map(int, input().split())
    events.append((s, 'start'))
    events.append((t + 1, 'end'))

# Sort: start before end if same position
events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else 1))

current_overlap = 0
max_overlap = 0

for _, event_type in events:
    if event_type == 'start':
        current_overlap += 1
        max_overlap = max(max_overlap, current_overlap)
    else:
        current_overlap -= 1

print(max_overlap)

