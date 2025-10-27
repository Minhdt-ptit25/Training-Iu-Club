n = int(input())
a = list(map(int, input().split()))
while len(a) > 0:
    print(min(a),end = ' ')
    a.remove(min(a))
#cách 2
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    # Hoán đổi phần tử nhỏ nhất về vị trí i
    a[i], a[min_idx] = a[min_idx], a[i]

# In kết quả
for x in a:
    print(x, end=' ')


