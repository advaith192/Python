cause=input("Do you have a medical cause? Say 'Y' or 'N': ")
attendance=int(input("Enter your attendance: "))
if cause == "Y":
    print("You can take the exam.")
else:
    if attendance >= 75:
        print("You can take the exam.")
    else:
        print("You cannot take the exam")