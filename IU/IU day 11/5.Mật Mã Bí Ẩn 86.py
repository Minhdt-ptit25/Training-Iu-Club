t = int(input())
for _ in range(t):
    n = input()
    if n[-1:] == '86':
        print(n[-2:])
        print("YES")
    else:
        print(n[-2:])
        print("NO")