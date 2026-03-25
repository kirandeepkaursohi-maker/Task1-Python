'''
>= 90, Grade A
80 and 89, Grade B
70 and 79 , Grade C
60 and 69 , Grade D
< 60, Grade F
'''

# if-elif-else

marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
else:
    print("Grade F")
print("Thanks")
