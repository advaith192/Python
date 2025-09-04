word=input("Enter the word: ")
letter="aeiouAEIOU"
count=0
for i in word:
    if i in letter:
        count+=1
print(count)

word=input("Enter the word: ")
letter="aeiouAEIOU"
string1=("")
for i in word:
    if i not in letter:
        string1=string1+i
print(string1)