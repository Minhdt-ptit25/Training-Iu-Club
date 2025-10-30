def reverse_num(n):
    re_num = ''
    while n > 0:
        re_num += str(n % 10)
        n //= 10
    return re_num
print(reverse_num(100))
