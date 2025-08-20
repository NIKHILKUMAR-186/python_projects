
def add(a,b):
        return a +b
    
def subtraction(a,b):
        return a-b
    
def multiplication(a,b):
        return a*b
    
def division(a,b):
        return a/b
    
try:
    operation = input("enter the operation you want to perform : " )
    number1 = int(input("enter the first number : "))
    number2 = int(input("enter the second number : "))
    if (operation== "+"):
        print(add(number1,number2))
    elif(operation== "-"):
        print(subtraction(number1,number2))
    elif(operation== "*"):
        print(multiplication(number1,number2))
    elif(operation=="/"):
        print(division(number1,number2))
    else:
        print("Invalid operation! Please choose from +, -, *, /.")
except ValueError:
      print("plese enter the correct operation!")
except ZeroDivisionError:
      print("calculation not possible!")
      