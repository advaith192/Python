def my_function(n):
    sum=0
    reversed_n = n[::-1]
    if reversed_n == n:
        return True
    else:
        return False

n=input("Enter a word: ")
print(my_function(n))