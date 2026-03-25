"""
if marks >= 60, student is Pass else 
student is fail
when student is pass, then we print Grade:
>= 90, Grade A
80 and 89, Grade B
70 and 79, Grade C
60 and 69, Grade D
"""

marks = float(input("Enter marks: "))
if marks >= 60:
    print("Pass P")
    if marks >= 90:
        print("Grade A")
    elif marks >= 80 and marks < 90:
        print("Grade B")
    elif marks >= 70 and marks < 80:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Fail F")
