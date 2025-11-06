list = [1,2,3,3,4,5,6,7,8,9,10]
print(max(list))
print(min(list))
list.append(11)
print(list)
print(list.count(3))
list2 = [5,6,7,8,9,25]
list.extend(list2)
print(list)
print(list.index(1))
list.insert(3,7)
print(list)
list.pop(5)
print(list)
list.remove(3)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)


list = [1,2,3,4,5,6]
newlist = []
for i in list:
    newlist.append(i*i)
print(newlist)