#exceptions = events detected during execution that interrupt the flow of a program.
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide from: "))
    result = numerator/denominator
except ZeroDivisionError:
    print("You can't divide by zero, Idiot!")
except ValueError:
    print("Only enter numbers plz!")
except Exception:
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute.")
