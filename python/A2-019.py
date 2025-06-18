message = list(input())
buu_count = 0
max_u_streak = 0
current_streak = 0
buu_sequence = ['B', 'U', 'U']

for i in range(0, len(message) -2):
    chunk = message[i:i+3]
    if chunk[0].lower() == 'b' and chunk[1].lower() == 'u' and chunk[2].lower() == 'u':
        buu_count += 1

for char in message:
    if char.lower() == 'u':
        current_streak += 1
        if current_streak > max_u_streak:
            max_u_streak = current_streak
    else:
        current_streak = 0

if buu_count > 0:
    print('Yes ' + str(max_u_streak)) 
else:
    if 'b' in message:
        b_index = message.index('b')
        for j in range(b_index + 1, len(message)):
            message[j] = 'U'
        print(''.join(message))
    elif 'B' in message:
        upper_b_index = message.index('B')
        for k in range(upper_b_index + 1, len(message)):
            message[k] = 'U'
        print(''.join(message))
    else:
        buu_list = [buu_sequence[a % len(buu_sequence)] for a in range(len(message))]
        message = buu_list
        print(''.join(message))
