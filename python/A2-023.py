from re import *

def max_a(s):
    s = s.lower()
    matches = findall(r'a+', s)
    return max((len(m) for m in matches), default=0)

message = list(input().replace(' ', ''))
pure_blood = False
false_index = 0

for i in range(len(message) - 1):
    current = message[i].lower()
    next_char = message[i + 1].lower()

    if (current == 'r' and next_char == 'a') or (current == 'b' and next_char in ['i', 't']):
        pure_blood = True
        break
    else:
        false_index += i
        break

if pure_blood:
    print('yes ' + str(max_a(''.join(message))))
elif not pure_blood:
    print('no ' + str(false_index))
else:
    print('unknown ' + str(len(message)))
