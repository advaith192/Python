lower=int(input("Enter a lower bound: "))
upper=int(input("Enter an upper bound: "))
print("The numbers that are prime are: ")
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)