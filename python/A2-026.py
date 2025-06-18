something = int(input())
overweight = 0
nw_list = []
overweight_weights = []

for _ in range(something):
    names_and_weight = input()
    parts = names_and_weight.split()

    if len(parts) == 2:
        nw_list.append(parts)

nw_list = [[name, int(weight)] for name, weight in nw_list]

for i in nw_list:
    for j in i:
        if isinstance(j, int) and j > 15:
            overweight += 1
            overweight_weights.append(j)

max_weight = max(overweight_weights)
for k, sublist in enumerate(nw_list):
    if max_weight in sublist:
        target_index = k
        break

overweight_mf = nw_list[target_index][0]
print(overweight)
print(overweight_mf, str(max_weight))
