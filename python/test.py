def max_a(s):
    import re
    return max((len(m) for m in re.findall(r'a+', s.lower())), default=0)

s = input().strip()
s_lower = s.lower()
n = len(s_lower)

# Check for 'unknown' case: only I and T letters
if all(c in 'it' for c in s_lower if c.isalpha()):
    print('unknown', n)
    exit()

i = 0
while i < n:
    c = s_lower[i]

    if c == 'r':
        # Must be followed by at least one A
        if i + 1 >= n or s_lower[i + 1] != 'a':
            print('no', i + 1)
            exit()
        i += 1
        while i < n and s_lower[i] == 'a':
            i += 1

    elif c == 'b':
        # Must be followed by at least one I or T
        if i + 1 >= n or s_lower[i + 1] not in 'it':
            print('no', i + 1)
            exit()
        i += 1
        while i < n and s_lower[i] in 'it':
            i += 1

    elif c == 'a':
        # A must be preceded by R
        if i == 0 or s_lower[i - 1] != 'r':
            print('no', i)
            exit()
        i += 1

    elif c in 'it':
        i += 1

    else:
        # Invalid character (not in R, A, B, I, T)
        print('no', i)
        exit()

print('yes', max_a(s))

