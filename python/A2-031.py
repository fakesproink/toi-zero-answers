def is_matching(a, b):
    return (a == 'A' and b == 'T') or (a == 'T' and b == 'A') or (a == 'C' and b == 'G') or (a == 'G' and b == 'C')

chromosome_length = int(input())
strand1 = input().split()
strand2 = input().split()
n = int(input())
mutations = []
not_matching_count = 0

for _ in range(n):
    mutation = input().split()
    for __ in range(len(mutation)):
        if mutation[__].isdigit():
            mutation[__] = int(mutation[__])
    mutations.append(mutation)

for strand_num, index, new_gene in mutations:
    if strand_num == 1:
        strand1[index] = new_gene
    else:
        strand2[index] = new_gene

for i, j in zip(strand1, strand2):
    if not is_matching(i, j):
        not_matching_count += 1

print(*strand1)
print(*strand2)
print(not_matching_count)
