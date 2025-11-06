def factorial(a):
    '''This is to factorialise a number'''
    if a == 0 or a == 1:
        return 1
    else:
        b = a * (factorial(a-1))
        return b
print(factorial(4))