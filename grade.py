.import sys
if len(sys.argv) != 6:
    print("Usage: python grade.py m1 m2 m3 m4 m5")
    sys.exit()
marks = list(map(float, sys.argv[1:6]))
avg = sum(marks) / 5
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "Fail"
print("Average Marks:", avg)
print("Grade:", grade)
