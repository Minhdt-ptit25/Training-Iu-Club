#Bài 1
n = int(input())
sum = 0
array = list(map(int, input().split()))
for i in range(n):
    if i % 2 != 0:
        sum += array[i]
print(sum)
#Bài 2
num = int(input())
array = list(map(int, input().split()))
lst = []
for i in range(n):
    for j in range(i+1,n):
        if array[i] == array[j]:
            lst.append(abs(i-j))
if len(lst) != 0:
    print(min(lst))
else:
    print(-1)
#Bài 3
for i in range(2):
    a,b,c = map(int,input().split())
    if a + b - c == 0 or a - b + c == 0 or b + c - a ==0:
        print('yes')
    else:
        print('no')
#Bài 4
phan_tu, truy_van = map(int,input().split())
for _ in range(phan_tu):
    array = list(map(int, input().split()))



