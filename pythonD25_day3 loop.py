#Bài 1: In ra các số chẵn từ 1 đến 100 bằng 2 cách dùng hàm range
#Cách 1
for i in range(2,101,2):
    print(i,end=" ")
print()
#Cách 2
for i in range(101):
    if i % 2 == 0 and  i > 0:
        print(i,end =" ")
print()
#Bài 2: Tính tổng các số từ 1 đến 10
sum = 0
for i in range(1,11):
    sum += i 
print(sum)
#Lặp với chuỗi string
name = "Minh"
for ki_tu in name:
    print(ki_tu, end=" ")
#Vòng lặp while
count = 0
while count < 10:
    print("Count =", count)
    count += 1
#break
n = 10
for i in range(n):
    if i == 6:
        break
    print(i)
#Continue
n = 10
for i in range(n):
    if i % 2 != 0:
        continue
    print(i)

#Else
n = 100
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        print("n không là số nguyên tố")
        break
else:
    print("n chính là số nguyên tố")
