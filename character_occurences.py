string=input("Enter a phrase: ")
letter=input("Enter a letter: ")
i=0
count=0
while (i<len(string)):
    if string[i] == letter:
        count+=1
    i+=1
print(count)