n = int(input())
a = list(map(int, input().split()))
k = int(input())

seen = set()
dem = 0
for num in a:
    if k - num in seen:
        dem += 1
    seen.add(num)
print(dem)
#2
dem = 0
