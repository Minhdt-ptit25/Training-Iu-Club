n = int(input())
for i in range(n):
    s = input()
    max_num = 0
    current = ''
    for letter in s:
        if '0' < letter < '9':
            current += letter
        else:
            if current:
                max_num = max(max_num, int(current))
                current = ''
if current:
    max_num = max(max_num, int(current))
print(max_num)

