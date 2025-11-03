t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n-k):
        a[i], a[i+k] = a[i+k], a[i]
    print(a)
    