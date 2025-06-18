n = int(input())
num_pairs = list(map(int, input().strip().split()))

# Check that the input is valid
if len(num_pairs) != 2 * n:
    print("Error: Expected", 2 * n, "numbers.")
    exit()

max_nums = []

for i in range(0, 2 * n, 2):
    a, b = num_pairs[i], num_pairs[i + 1]
    max_nums.append(max(a, b))

if len(max_nums) == 1:
    print(max_nums[0])
else:
    print(' + '.join(map(str, max_nums)) + " = " + str(sum(max_nums)))

