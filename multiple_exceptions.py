try:
    num1,num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2
    print(result)
except ValueError:
    print("Use number not text")
except ZeroDivisionError:
    print("Don't divide by 0")
except SyntaxError:
    print("You forgot the comma")
else:
    print("No exceptions")