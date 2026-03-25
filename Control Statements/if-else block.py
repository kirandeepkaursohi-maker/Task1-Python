#if-else

#if condition:
#    #executed when condition: True
#else:
#    #executed when condition: False

age = float(input("What is your age? "))
if age >= 18:
     print("You are old")
else :
     print("You are underage")
print("thanks")


#Print if a number (int) is odd or even
#Even - when number is /2
#odd - when number is not /2

number = int(input("Type Number: "))
if number  % 2 == 0:
    print("You are an even number")
else:
    print("You are an odd number")
print("thanks")

#Print if Number is Negative or Positive

num = int(input("Type Number: "))
if num > 0:
    print("You are an positive number")
else:
    print("You are a negative number")
print("thanks")