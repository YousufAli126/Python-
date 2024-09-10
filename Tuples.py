# Tuples
#* (), ordered and unchangeable, allows and duplicates and is faster.

student = ('Yousuf', 16, 'Male')
print(student.count("Yousuf"))
print(student.index("Male"))

for x in student:
    print(x)

if 'Yousuf' in student:
    print("Yousuf is here!")
else:
    print("Yousuf is not here!")