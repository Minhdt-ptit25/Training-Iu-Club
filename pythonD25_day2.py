#in ra chuỗi
print("D25 Dinh Tuan Minh")
#in ra các đối tượng
print("D25", "Dinh", "Tuan", "Minh", sep="--", end="!\t")
#in ra tuple
x = ("apple", "banana", "cherry")
print(x)
# Yêu cầu người dùng nhập tên
name = input("Nhập tên của bạn: ")
print("Hello, " + name + "!")
# Yêu cầu người dùng nhập một số nguyên
number = int(input("enter an interger: "))
print("Your interger is:", number)
#chương trình tính tổng hai số
num1 = int(input("nhập số tuổi người thứ 1: "))
num2 = int(input("nhập số tuổi người thứ 2: "))
sum = num1 + num2
print("Tổng số tuổi của cả 2 người là:", sum)
#toán tử số học
a = 29
b = 84
print("a + b:", a + b)    
print("a - b:", a - b)    
print("a * b:", a * b)    
print("a / b:", a / b)     
print("a % b:", a % b)    
print("a ** b:", a ** b)   
print("a // b:", a // b)   
#toán tử so sánh 
n = 34
m = 65
print("n == m:", n == m)   
print("n != m:", n != m)  
print("n > m:", n > m)     
print("n < m:", n < m)     
print("n >= m:", n >= m)   
print("n <= m:", n <= m) 
#toán tử gán
i = 75
i += 11
print("i += 11:", i)
i -= 3
print("i -= 3:", i)
i *= 34
print("i *= 34:", i)
i /= 5
print("i /= 5:", i)
i %= 9
print("i %= 9:", i)
i **= 13
print("i **= 13:", i)
i //= 21
print("i //= 21:", i)
#toán tử logic
c = True
d = False
print("c and d:", c and d)   
print("c or d:", c or d)     
print("not c:", not c)       
age = int(input("Nhập số tuổi của bạn: "))
if age >= 18:
    print("Bạn đã đủ tuổi bỏ phiếu\nĐủ tuổi lấy vợ, lấy chồng\nKết thúc if!")
else:
    print("Bạn chưa đủ tuổi bỏ phiếu\nLấy vợ, lấy chồng là vi phạm pháp luật\nKết thúc else!")
print("Kết thúc chương trình")
score = int(input("Nhập số điểm của bạn: "))
if score >= 90:
    print("Điểm của bạn thuộc hạng A")
elif score >= 80:
    print("Điểm của bạn thuộc hạng B")
elif score >= 70:
    print("Điểm của bạn thuộc hạng C")
else:
    print("Điểm của bạn thuộc hạng F")

