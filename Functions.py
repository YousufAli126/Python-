# Functions
#def hello(name):
    #print("HellO! "+name)
    #print("Have a nice day!")

#name = "Yousuf"

#def hello(first_name, last_name, age):
    #print("Hello! "+first_name+" "+last_name)
    #print("You are " +str(age)+ " years old.")

#hello('Yousuf', 'Ali.', 16)

# Return statement
#def multiply(num1, num2):
#   result = num1 * num2
#    return result

#x = multiply(2,5)
#print(x)

#def multiply(num1, num2):
    #return num1 * num2

#x = multiply(2,5)
#print(x)

#Keyword arguments
#def hello(first,middle,last):
#    print("Hello, "+first+" "+middle+" "+last)

#hello(first='Yousuf',middle='Ali',last='Khan.')

#Nested Function Calls
#print(round(abs(float(input("Enter a whole number: ")))))

#* *args : parameter that will pack all arguments into a dictionary
#*       useful so that a function can accept a varying amount of positional arguments

#*def add(*math):
#*    '''This is not a comment'''
#*   sum = 0
#*   math = list(math)
#*    math[0] = 0
#*    for i in math:
#*        sum += i
#*   return sum
#*print(add(1,2,3,4,5))

#? **kwargs : parameter that will pack all arguments into a dictionary
            #? useful so that a function can accept a varying amount of keyword arguments

#?def user(**name):
#?    print("Hello, " + name['first'] + " " + name['last'])
#?     print("Hello,", end=" ")
#?     for key,value in name.items():
#?        print(value, end=" ")
#? user(title='Mr.', first='Yousuf', middle='Ali', last='Khan.')

#~  Recursion : A function that can call itself is called a recursive function.
#~ factorial(7) = 7*6*5*4*3*2*1
#~ factorial(6) = 6*5*4*3*2*1
#~ factorial(5) = 5*4*3*2*1
#~ factorial(4) = 4*3*2*1
#~ factorial(3) = 3*2*1
#~ factorial(2) = 2*1
#~ factorial(0) = 1
#~ factorial(n) - n * factorial(n-1)
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))
print(factorial(6))
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))

#~ 7 * factorial(6)
#~ 7 * 6 * factorial(5)
#~ 7 * 6 * 5 * factorial(4)
#~ 7 * 6 * 5 * 4 * factorial(3)
#~ 7 * 6 * 5 * 4 * 3 * factorial(2)
#~ 7 * 6 * 5 * 4 * 3 * 2 * factorial(1)
#~ 7 * 6 * 5 * 4 * 3 * 2 * 1



