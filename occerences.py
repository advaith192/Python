word=input("Enter the word: ")
letter=input("Enter the letter: ")
count=0
for i in word:
    if i in letter:
        count+=1
print(count)