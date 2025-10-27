from math import *
#hàm snt 
def snt(n):
    if n < 2:
        return 0
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return 0
    return 1

#ham tong chu so cua n 
def sum(n):
    tong = 0
    while n != 0:
        tong += tong // 10
        n //= 10
    return tong
#in ra tong chu so chan cua n
def tong_chan(n):
    tong = 0
    while n != 0:
        if n % 10 % 2 == 0:
            tong += n % 10    
            n //= 10
    return tong
#in ra tong chu so nguyen to
def sum_Prime(n):
    tong = 0
    while n != 0:
        r = n % 10
        if r == 2 or r == 3 or r == 5 or r == 7:
            tong += r
        r //= 10
    return tong
#in ra so lat nguoc cua n
#cach 1
def solatnguoc(n):
    n = str(n)[::-1]
    return n
#cach2
def hamnguoc(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
#dem so luong uoc nguyen to
def count_prime(n):
    dem = 0
    for i in range(2,int(n ** 0.5)+ 1):
        if n % i == 0:
            dem += 1
            while n % i == 0:
                n //= i
    if n > 1:
        dem += 1
    return dem
#hàm snt lon nhat
def max_prime(n):
    res = -1 
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            res = i 
            while n % i == 0:
                n //= i
    if n > 1:
        res = n
    return res
def check_prime_6(n):
    while n != 0:
        if n % 10 == 6:
            return 1
        n //= 10
    return 0
#tong chu so chia het cho 8
def tong_chia_het_8(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    if tong % 8 ==0:
        return 1
    else:
        return 0
#tinh tong giai thua 
def tong_giai_thua(n):
    tong = 0
  
    while n != 0:
        digits = n % 10
        gt = 1
        for i in range(1,digits+1):
            gt *= i    
        tong += gt
        n //= 10 
    return tong
#kiem tra day 1 so

        




        

    
  
