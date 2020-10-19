input_list = []
base = 17
totalInput = int(input("Size of Input:"))

for i in range(1, totalInput + 1):
    n = input()
    input_list.append(n)

size = len(input_list)
print(input_list, size)
ans = 0
for i in input_list:
    size = size - 1
    print(i, base, size)
    if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        ans += int(i) * (base ** size)
    elif i == 'A':
        ans += 10 * (base ** size)
    elif i == 'B':
        ans += 11 * (base ** size)
    elif i == 'C':
        ans += 12 * (base ** size)
    elif i == 'D':
        ans += 13 * (base ** size)
    elif i == 'E':
        ans += 14 * (base ** size)
    elif i == 'F':
        ans += 15 * (base ** size)
    elif i == 'G':
        ans += 16 * (base ** size)
print(ans)
