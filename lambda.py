#hàm lambda ẩn danh
lam = lambda x,y,z: x + y + z
print(lam(1,2,3))
#filter
c = [3, 2, 5, 6]
a = list(filter(lambda x:x % 2 == 0,c))
print(a)