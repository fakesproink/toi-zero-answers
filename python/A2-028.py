student_id_length = int(input())
first_student_id = list(input().strip())
second_student_id = list(input().strip())
idk_count = 0
idk2_count = 0

first_student_id = [int(_) for _ in first_student_id]
second_student_id = [int(__) for __ in second_student_id]

for i, j in zip(first_student_id, second_student_id):
    if i + j == 9:
        idk_count += 1
    else:
        idk2_count += 1

if idk_count == student_id_length:
    print('YES')
else:
    print('NO ' + str(idk2_count))
