n = int(input().strip())
n_string = str(n)
counter = 0
zero_counter = 0
zeros = []
expanded = []
expanded_roman = []

roman_lookup = {
    0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    3: ["", "M", "MM", "MMM"]
}

if len(str(n)) > 4 and n > 3999:
    print("error")

for i in n_string:
    counter += 1
    if int(i) == 0:
        pass
    else:
        expanded.append(str(i) + ('0' * (len(n_string) - counter)))

for j in expanded:
    zero_counter = 0
    for k in j:
        if '0' in k:
            zero_counter += 1
    zeros.append(zero_counter)

for idx, zero_count in enumerate(zeros):
    digit = int(expanded[idx][0])
    if zero_count in roman_lookup:
        roman_part = roman_lookup[zero_count][digit]
        expanded_roman.append(roman_part)

print("".join(expanded_roman))
