n = 10
for i in range(n):
    for space in range(n-i-1,0,-1):
        print(" ",end="")
    for star in range(2*i + 1):
        print('*',end = "")
    print()
print()
#tam giác đều
for i in range(n):
    if i == 0:
        print(' '*(n-i-2)+'*')
    elif i > 1:
        print(' '*(n-i-1) + ("*"+" ")*(i))