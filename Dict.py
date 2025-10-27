#Cấu trúc khai báo, khởi tạo
my_dic = {
    'name':'minh',
    'age':18,
    'school' :'PTIT'
}
print(my_dic)
print(my_dic['name'])
print(my_dic['age'])
print(my_dic['school'])
#print(my_dic['heheboiz']) #key error
#Sử dụng với phương thức get
# value =  my_dic.get(key, default value)
print(my_dic.get('name','none'))
print(my_dic.get('sex','N/A')) # giá trị sau key tức là trả về nếu key k dc tìm thấy
#Lấy dánh sách khóa,giá trị,cặp khóa, giá trị
student = {
    'name' : 'Minh',
    'age': 18
}
print(student.keys())
print(student.values())
print(student.items())
#Nest Dict
san_pham = {
    "sua" : {'name':"TH true milk",'price':18},
    'banh': {'name':"Cosy",'price':36},
    'traicay':{'name':'tao','price':40}
}
print(san_pham['sua']['price'])
#Thêm cập nhật và xóa phần tử
student['name'] = 'minhdinhtuan'#cập nhật lại tên

student['sex'] = 'male'#thêm mới key và value

print(student)
#Xóa phần tử
del my_dic['name']
print(my_dic)
result = my_dic.pop('age','default')
print(result)