n=int(input("Enter a number: "))
sum=0
temp = n
while temp > 0:
    digits = temp % 10
    sum += digits ** len(str(n))
    temp = temp // 10
if sum == n:
    print("This is an armstrong number")
else:
    print("This is not an armstrong number")