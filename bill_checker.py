def total_amount(bill_amount,tip):
    total = bill_amount + tip
    total = round(total,2)
    return total

print(total_amount(150,20))