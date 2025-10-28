import math
#hàm chia tách các số
# so sánh với n nếu đúng return yes else no

def facsum_split_num(n):
    old_num = n
    ans = 0
    while n > 0:
        ans += math.factorial(n % 10)
        n //= 10
    if ans == old_num:
        return('Yes')
    else:
        return('No')

t = int(input())
for _ in range(t):
    num = int(input())
    print(facsum_split_num(num))
