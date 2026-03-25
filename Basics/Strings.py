s1 = "Hello World"
print(s1)

print(len(s1))
print("First char", s1[0])
print("Second char", s1[1])
'''
#Syntax of Indexing: string[index]
#Syntax of Slicing: string[start:end:step]
'''

print(s1[2:12:3])
s1_slice = s1[2:12:3]
print(s1_slice)
print(type(s1_slice))


#Escaping in Sequence
#\n
print("Hello Everyone.\nHow are You?")

#\t
print("Kiran 25")
print("Kiran\t25")

#\\
print("new\\old")

#\'
print('This is a Python\'s class')



#FString
name = "Kiran"
age = 25
language = ("Python")
hours = 3

print(name, "is", age, "years old")

print(f"{name} is {age} years old")
sub1= "english "
sub2 = "math "
sub3= "punjabi "

total= sub1 + sub2 + sub3
print(f"{name} have three subjects named: {total}")


s1 = "Python is Fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python "
version = "3.13.3 "
print(language + version)
#print("Python" - "P")
print(s1 * 2)

#Membership operation
#in
print("Python" in s1)
print("1" in s1)
s2= s1.strip()
print(s2)

#strip()
name = "Kiran "
newname = name.strip()
print(newname)

# replace()
print(name.replace("Kiran", "Karan"))
print(name.replace("i", "a"))

#count() Counting substring from a string
a1= "I am Kiran. Kiran is 25 years old. Kiran studies CSE."
s2= "Kiran"
print(a1.count(s2))
print(a1.count("i"))
print(a1.count("Ki"))

#case- Changing case of a string
print(s2.upper())
print(s2.lower())
print(s2.title())
print("i am learning python".title())
print(a1.capitalize())

#Starting and ending string
# startswith()
print(a1.startswith("I"))
print(a1.startswith("K"))

# endswith()
print(a1.endswith("CSE."))

