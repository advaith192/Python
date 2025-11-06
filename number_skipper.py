var = int(input("Enter a value: "))
var1 = int(input("Enter another value to skip: "))
i = var
while i > 0:
    i-=1
    if i == var1:
        continue
    print(i)