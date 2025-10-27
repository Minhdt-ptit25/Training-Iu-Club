import re 
print(r'sdfkjf\sdff')# xử lý chuỗi thô
pattern = re.compile(r'trinh$')
text_data = '''
kjsh gjdfjskfkgjffgsdkfgsdkjgds
fgdflkjjghdskfghskjdfg
dfkjgsdfhgksdfgkjhdsfg
djfkgshdflkghskfgh
rtkwjer ruhtwkelrwe
sabcdef
defabd
yabc
ABC
abc
 Giới thiệu về Module re trong Python: Tìm hiểu về các hàm và chức năng cơ bản.
✅ Cú pháp Regex trong Python: Cách xây dựng và sử dụng biểu thức chính quy đơn giản.
✅ Các hàm cơ bản của module re: re.match, re.search, re.sub, re.split và nhiều hơn nữa.
✅ Ví dụ thực tế: Làm việc với các ví dụ nh][ươ]ơ]][[[ơ]ưư kiểm tra email, URL và xử lý chuỗi văn bản.
✅ Cách sử dụng các phương thức .s45786237456324tart, .end, .group, .span để lấy thông tin từ kết quả tìm kiếm Regex.'''

sentence = 'Xin chao toi dang hoc lap trinh'



datas = re.finditer(pattern,sentence)
for data in datas:
    print(data)

# , [ { ( ) \ ^ $ | ? * +
