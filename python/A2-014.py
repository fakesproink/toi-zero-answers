from itertools import *

def match_length(list1, list2):
    max_len = max(len(list1), len(list2))
    new_list1 = list(islice(cycle(list1), max_len))
    new_list2 = list(islice(cycle(list2), max_len))
    return new_list1, new_list2

name1 = list(input())
name2 = list(input())
sl_name1, sl_name2 = match_length(name1, name2)
result = []
w_count = 0
w_bursts = []

for i, j in zip(map(str.lower, sl_name1), map(str.lower, sl_name2)):
    if i == 'l' or j == 'l' or i == 'o' or j == 'o' or i == 'v' or j == 'v' or i == 'e' or j == 'e':
        result.append('w')
    else:
        result.append('$')

# check w count and do whatever
for k in result:
    if k == 'w':
        w_count += 1

if w_count % 2 != 0:
    # check for w bursts
    count = 0
    for a, c in enumerate(result):
        if c == 'w':
            count += 1
        else:
            if count >= 2:
                w_bursts.append([count, 1])
            count = 0

    if count >= 2:
        w_bursts.append([count, 1])

    result.append(str(max([item for sublist in w_bursts for item in sublist])))
else:
    if not any(result[b] == 'w' and result[b + 1] == 'w' for b in range(len(result) - 1)):
        result.append('#')

print(''.join(result))
