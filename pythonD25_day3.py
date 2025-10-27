age = int(input("nhập số tuổi của bạn: "))
sex = 'male'
if age >= 18:
    if sex == 'male':
        print("Bạn đã đủ điều kiện đi nghĩa vụ quân sự")
        print("Bạn đã đủ tuổi lấy vợ")
    else:
        print("Bạn không phải là nam")
        print("Bạn không bắt buộc đi nghĩa vụ quân sự")
else:
    if sex == 'male':
        print("Bạn chưa đủ điều kiện đi nghĩa vụ quân sự")
        print("Bạn chưa đủ tuổi lấy vợ")
    else:
        print("Bạn không bắt buộc đi nghĩa vụ quân sự")
        print("Bạn chưa đủ tuổi lấy chồng")
#6.Kết hợp điều kiện với các toán tử logic
tuoi = int(input())
nationality = 'Vietnamese'

if tuoi >= 18 and nationality == 'Vietnamese':
    print("Bạn đủ điều kiện để bỏ phiếu.")
else:
    print("Bạn không đủ điều kiện để bỏ phiếu.")
#7.Ứng dụng điều kiện với các kiểu dữ liệu khác nhau
x = int(input("Nhập giá trị x: "))
y = int(input("Nhập giá trị y: "))

if x < y:
    print("x nhỏ hơn y")
elif x > y:
    print("x lớn hơn y")
else:
    print("x bằng y")
#7.2 Điều kiện với chuỗi
name = "Minh"
if name == "Minh":
    print("Xin chào Minh,tri kỉ của mình")
else:
    print("Xin chào bạn,rất vui khi làm quen với bạn")