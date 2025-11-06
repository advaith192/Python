def my_function(words):
    count = 0
    empty_list = []
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
            empty_list.append(i)
    print("The words are: ",empty_list[0],"and",empty_list[1], "with a count of", count)

words = ["racecar","hello", "hi", "phone", "laptop", "glag"]
my_function(words)