n = int(input())
dic = {}
for i in range(n):
    s = int(input())
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
print(dic)

