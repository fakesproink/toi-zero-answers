bowl_count = int(input())
bowl_sizes = [int(input()) for _ in range(bowl_count)]
stacks = []

for b in bowl_sizes:
    best_stack = None
    best_top = float('inf')

    for stack in stacks:
        top = stack[-1]
        if b < top and top < best_top:
            best_top = top
            best_stack = stack

    if best_stack:
        best_stack.append(b)
    else:
        stacks.append([b])

print(len(stacks))
