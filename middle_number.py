num=input("Enter a number: ")
length=len(num)
if length % 2 == 1:
    mid=length//2
    print(num[mid])
else:
    mid1=(length//2)-1
    mid2=length//2
    print(int(num[mid1]) * int(num[mid2]))