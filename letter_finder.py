word = input("Enter a word: ")
letter = input("Enter a letter: ")
for i in word:
    if i == letter:
        print("Letter found")
        break
else:
    print("Letter not found")