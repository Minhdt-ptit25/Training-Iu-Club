a = list(map(int, input().split()))
for i in range(1,max(a)+1):
    if i not in a:
        print(i,end = ' ')
