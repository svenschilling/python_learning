# SLICING : UP TO BUT NOT INCLUDING!!!!!

a = [3,4,-10]
a.append(2)
print(a)
# append another list
a.append(["ich","bin",23])
print(a[5])
b = ["banana", "apple", "python"]
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
b[0], b[2] = b[2], b[0]
print(b)