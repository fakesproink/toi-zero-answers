score_count = int(input())
scores = []
top_score_count = 0

for _ in range(score_count):
    score = int(input())
    scores.append(score)

for i in scores:
    if i == max(scores):
        top_score_count += 1

print(max(scores))
print(top_score_count)
