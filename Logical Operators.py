# 9. LOGICAL OPERATORS
temp = int(input("What is the temperature?: "))
if not temp >= 0 and temp <= 30:
    print("The temperature is good.")
    print('You should go out.')
elif not temp < 0 or temp > 30:
   print("The temperature is bad.")
   print("Stay inside.")
