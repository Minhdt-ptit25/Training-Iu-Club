def sort_num(n):
    lst = []
    str_n = str(n)
    for i in range(len(str_n)-1):
        if str_n[i].isdigit():
            if str_n[i+1].isdigit():
                new_val = str_n[i]
                new_val += str_n[i+1]
                lst.append(new_val)
                continue
            elif not str_n[i+1].isdigit():
                lst.append(str_n[i])
    lst.sort()
    return lst
t = int(input())
for _ in range(t):
    n = input()
    print(sort_num(n),end = '\n')
