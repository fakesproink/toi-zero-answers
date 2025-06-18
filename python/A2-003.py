n = int(input().strip())
tree_heights = list(map(int, input().split()))
favored_trees = 0
error = False

if len(tree_heights) != n or len(tree_heights) != len(set(tree_heights)) or any(t < 1 or t > 1000000 for t in tree_heights):
    error = True
    print('error')
elif not error:
    for i in range(len(tree_heights)):
        if i == 0:
            if tree_heights[i] > tree_heights[i + 1]:
                favored_trees += 1
        elif i == len(tree_heights) - 1:
            if tree_heights[i] > tree_heights[i - 1]:
                favored_trees += 1
        else:
            if tree_heights[i] > tree_heights[i - 1] and tree_heights[i] > tree_heights[i + 1]:
                favored_trees += 1

    print(favored_trees)
