score = int(input("Enter your exam score (0-100): "))
bonus = int(input("Enter bonus points (0-10): "))
final_score = score + bonus
if final_score >= 90 and final_score <= 100:
    print("Grade: 9")
elif final_score >= 75 and final_score < 90:
    print("Grade: 8")
elif final_score >= 50 and final_score < 75:
    print("Grade: 7")
elif final_score >= 0 and final_score < 50:
    print("Grade: 1")
else:
    print("Invalid score entered")