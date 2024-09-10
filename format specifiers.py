#Format Specifiers
#* :.(num)f = round to given num of decimal places
#* :(number) = allocate that many spaces
#* :03 = allocates and zero pad that many spaces
#* :< = left justify
#* :> = right justify
#* :^ = center align
#* :+ = indicates positive values
#* :, = separate large values by putting comma
#* := = place sign to leftmost position
#* :  = inserts a space before positive numbers

value1= 69966699.9669
value2= 16978425.52523
value3= -5271252.1475

print(f'Value 1 is {value1:^+,.2f}')
print(f'Value 2 is {value2:^+,.2f}')
print(f'Value 3 is {value3:^+,.2f}')