# 8. IF...ELSE  STATEMENTS
age = int(input("Enter your age: "))
if age < 14:
    print("You are a child.")
elif age == 100:
    print('Congrats!!You have lived a century.')
elif age > 18:
    print("You are an adult.")
else:
    print("You are a teenager.")