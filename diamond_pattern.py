n = int(input("Enter the number of rows: "))
if n % 2 == 0:
    m = n//2
else:
    m = n//2 + 1
for i in range(1,m+1):
    spaces = " " * (m - i)
    numbers = ""
    for x in range(1,2*i):
        numbers = numbers + str(x)
    print(spaces + numbers)
for i in range(1,m):
    spaces = " " * i
    numbers = ""
    for x in range(1,2*(m-i)):
        numbers = numbers + str(x)
    print(spaces + numbers)