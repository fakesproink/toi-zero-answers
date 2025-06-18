l = int(input())
n = int(input())
layers = [(i * i) for i in range(1, l + 1)]
layers.reverse()

index = 0
while n > 0 and index < len(layers):
    if n >= layers[index]:
        n -= layers[index]
    else:
        n = 0

remaining_layers = len(layers) - index
print(remaining_layers)
