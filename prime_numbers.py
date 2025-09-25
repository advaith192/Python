def my_function(a):
    if a <= 1:
        return False
    else:
        for i in range(2,a):
            if a % i == 0:
                return False
        else:
            return True
a=int(input("Enter a number: "))
print(my_function(a))