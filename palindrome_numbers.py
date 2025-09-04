n=input("Enter a number: ")
sum=0
reversed_n = n[::-1]
if int(reversed_n) == int(n):
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")