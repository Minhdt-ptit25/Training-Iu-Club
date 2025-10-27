n = int(input('nhap so: '))
sum = 0
while n <= 0:
    n = int(input('nhap lại so: '))
if n > 0:
    for i in range(1, n + 1):
        sum += i
    if sum % 2 == 0:
        print("So chan")
    else:
        print("So le")