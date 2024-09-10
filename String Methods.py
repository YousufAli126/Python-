
#! 3. String Methods
# name = 'Yousuf Ali! '
# print(name.find("o")) #* Finds specific character in string.
# print(name.find("s"))
# print(len(name)) #* Tells length of a string.
# print(name.capitalize()) #* Makes first letter capital and converts others into lowercase
# print(name.upper()) #* converts all letter to uppercase/capital
# print(name.isupper()) #* tells if string is in uppercase
# print(name.islower()) #* tells if string is in lowercase
# print(name.lower()) #* converts all capital/uppercase letters to lowercase/small
# print(name.isdigit()) #* boolean, tells if string is a digit
# print(name.isalpha()) #* boolean, tells if a string is alphabetic
# print(name.isalnum()) #* boolean, tells if string is alpha-numeric
# print(name.rstrip("!")) #* removes last character/whitespaces
# print(name.split(' ')) #* shows a list with sub-strings of the string
# print(name.count("o")) #* counts how many times a character appears in a string
# print(name.replace('f','p')) #* replaces a character with another character
# print(name.center(50)) #* moves string towards centre, depends on how much we want to move it to center by writing number of spaces.
# print(name*3) #* multiples string
# print(name.startswith("Yousuf")) #* tells if string starts with the given character
# print(name.endswith(' ')) #* tells if the given character is ending of the string, (boolean)
# print(name.endswith("!", 4, 7))
# print(name.isprintable()) #* tells if string is printable, not printable if it has a escape sequence.
# print(name.isspace()) #* tells if there is a space or spaces in a string
# print(name.istitle()) #* tells if string is a title (is capitalized)
# print(name.title()) #* converts string into a title
# print(name.swapcase()) #* converts uppercase to lowercase and lowercase to uppercase

#! 7. String Slicing
# name = 'Yousuf Ali'
# first_name = name[:6]
# last_Name = name[7:]
# invalid_name = name[0:10:2]
# reverse_name = name[::-1]
# print(reverse_name)

# website1 = "https://google.com"
# website2 = "https://wikipedia.com"
# slice = slice[8,-4]
# print(website1[slice])
# print(website2[slice])

#! Match Case Statements: Compares a variable with all patterns 
# age = int(input("Enter your age: ")) 
# #* age is the variable to match
# match age:
#     #* if x is 0 
#     case 0:
#         print("Welcome to this world!!!")
#     #* case with if condition
#     case _ if age>0 and age<18:
#         print('Your a child or teenager.')
#     case _ if age>=18:
#         print("You are an adult.")
#     case _ : #* it is the default case only if above cases are not matched, like else
#         print(age)
        

#! String Format():

#! game = 'Counter-Strike'
#! console = 'PC'
#! print("My most fav {} game is {}.".format(console, game))
#! print("My most fav {1} game is {0}.".format(game, console)) # positional argument
#! print("My most fav {console} game is {game}.".format(console = 'PC', game = 'Counter-Strike')) # keyword argument


