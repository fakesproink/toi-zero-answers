arrays = []
ok_lists = []
history = []

for _ in range(5):
    array = list(map(int, input().split()))
    arrays.append(array)

for i in arrays:
    counter = 0

    for j in i:
        counter += j

    if counter % 2 == 0:
        ok_lists.append(True)
    else:
        ok_lists.append(False)

for k in ok_lists:
    if k == False:
        bad_list_index = ok_lists.index(k)
        item_sum = 0

        for a in arrays[bad_list_index]:
            item_sum += a
            history.append(item_sum)

for b in history:
    if b == max(history) and max(history) % 2 != 0:
        impostor_index = history.index(b) + 1
        break

if False in ok_lists:
    print(str(ok_lists.index(False)) + ' ' + str(impostor_index))
else:
    print('-1 ' + '-1')
