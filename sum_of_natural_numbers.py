def sum_of_natural_numbers(a):
    if a == 1:
        return 1
    else:
        return a + (sum_of_natural_numbers(a-1))
print(sum_of_natural_numbers(5))