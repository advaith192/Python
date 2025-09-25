def my_function(a):
    letter="aeiouAEIOU"
    count=0
    for i in a:
        if i in letter:
            count+=1
    return count
a=input("Enter a word: ")
print(my_function(a))