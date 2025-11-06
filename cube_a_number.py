def cube(a):
    cube1 = a**3
    return cube1

def mod(a):
    if a % 3 == 0:
        return cube(a)
    else:
        return False
print(mod(3))
print(mod(4))
print(mod(9))