def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
def hieu_luan_phien(n):
    n = reverse(n)
    ru = -1
    sum = 0
    while n > 0:
        char = 0
        char += n % 10 
        sum += char * ru
        ru *= -1
        n //= 10
    return sum
a = 12345
print(hieu_luan_phien(a))

