students = ["Binh","Nguyen","Thao","Dinh","Vo"]
for i in range(len(students)):
    print(i,students[i])
print()
for student in students:
    print(student, end = ' ')
print()
#
animals = ['chó','gà','vịt','lợn','sư tử','lạc đà']
print("Trước khi chỉnh sửa: ",animals)
animals[0] = 'voi'
print("Sau khi chỉnh sửa: ",animals)
copy_animals = animals.copy()
animals[2] = 'vượn'
print(copy_animals)
print(animals)
#Thay đổi nhiều phần tử trong list
my_list = [17,29,34,38]
my_list[1:2] = [22,33]
print(my_list)
#Thay đổi phần tử bằng vòng lặp
lst = [10,20,30,40,50]
for i in range(len(lst)):
    lst[i] += 2
print(lst)
#Thay đổi phần tử bằng list comprehention
arr = [10,20,30,40,50]
my_lst = [x+2 for x in arr]
print(my_lst)
#Thay đổi phần tử bằng map và lambda
mylist = [11,22,33,44,55]
mylist = list(map(lambda x: x + 2,mylist))
print(mylist)
#Enumerate
lst_1 = [1,2,3,4,5,6]
for index,value in enumerate(lst_1):
    print(index,value)
    lst_1[index] = value + 2
print(lst_1)
#Thay đổi phần tử bằng hàm replace
def replace(lst_2, old_val, new_val):
    return [new_val if x == old_val else x for x in lst_2]
lst_2 = [6,7,8,9,10]
lst_2 = replace(lst_2,6,56)
print(lst_2)
#Thay đổi phần tử bằng list lồng nhau
lst_3 = [[10,20,30],[40,50,60],[70,80,90]]
lst_3[0][1] = 21
lst_3[2][2] = 106
print(lst_3)
#Thay đổi phần tử bằng filter
lst_4 = [1,2,3,4,45,5,6,7,8,9,10]
lst_4 = list(filter(lambda x: x % 2,lst_4))
print(lst_4)
#Thêm phần tử vào danh sách
lst_5 = [1,2,3,4,5,6,7,8,9]
lst_5.append(10)
lst_5.append([5,10])
print(lst_5)
lst_5.extend([15,20])
print(lst_5)
print(lst_5 + [25,30])
#chèn phần tử vào vị trí cụ thể
Animal = ['cat','dog','fox']

animal_1 = 'dog'
print(animal_1)
Animal.insert(1, animal_1)
print(Animal)
#Nối danh sách
lst_6 = [1,2,3]
lst_7 = [4,5,6]
print(lst_6 + lst_7)
#Dùng * nối danh sách
# Tạo hai danh sách
List1 = [1, 2, 3]
List2 = [4, 5, 6]
new_list = [*List1, *List2]

# In danh sách mới
print(new_list)