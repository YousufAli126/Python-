# 10. WHILE LOOPS
while 1==1:
    print("Help! I'm stuck in a loop.")
name = None

while not name:
    name = input("Enter your name: ")
    
print("Hello,"+name)

# 11. FOR LOOPS
for i in range(10):
    print(i + 1)
for i in range(50,100 + 1,10):
    print(i)
import time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!")

# 12. NESTED LOOPS
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
   for j in range(columns):
       print(symbol, end="")
   print()

# 13. BREAK, CONTINUE AND PASS
while True:
    name = input("Enter your name: ")
    if name != "" :
        break

num = "123-456-7890"

for i in num:
    if i == "-":
        continue
    print(num)

for i in range(1,101):
    if i == 69:
        pass
    print(i)