# 1. Variables
#first_name = 'Yousuf'
#last_name = 'Ali'
#full_name = first_name +" "+ last_name

#age = 15
#age += 1

#print(f"Hello, {full_name}, you are {age} years old.")

#animal = False 
#print(animal)
#print("Are you an animal?",str(animal))

# Variable Scope

name = "Yousuf" # Global variable scope 

def no_name():
    name = 'Ali' #Local variable scope 
    print(name)

print(name)
no_name()