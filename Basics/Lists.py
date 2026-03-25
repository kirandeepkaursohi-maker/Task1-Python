name = "Kiran"
age = 25
study = "CSE"

student = ["John", 20, "CSE"]
print(type(student))
print(student)


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week[4])
print(days_of_week[-1])
print(f"Last day of week is {days_of_week[-1]}")
print(len(days_of_week))

print(days_of_week[4])
#can't print cause it is out of range of the list

#list operations
#slicing of lists
l1 = [1, 2, 3, 4, 5, 6]
print(l1[1:7:2])

#concatentation of lists
l1 = [1, 2, 3, 4, 5, 6]
l2 = ["a", "b", "c", "d", "e", "f"]
print(l1 + l2)

#repeat "*"
print(l1*2)

#append()
(l1.append(
    "numbers"))
print(l1)

#insert()
l1.insert(3, "Four")
print(l1)

#extend
l1.extend(["one", "two"])
print(l1)

print(len(l1))

#remove
l1.remove("numbers")
print(l1)

#pop
l1.pop(3)
l1.pop(-2)
print(l1)
l1.pop()
print(l1)

#reverse
l1.reverse()
print(l1)

#sort
l2= [4,2,9,10,30,23,21]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)

#count
l3 = l1 + l2
print(l3)
print(l3.count(4))

#membership operation
#in
print(23 in l3)
print(23 not in l3)

#to find smallest or minimum number of list
print(min(l3))
#to find biggest number
print(max(l3))

#sum() to find total of the numbers
print(sum(l3))


#Nested Lists
l4 = [1, 2.3, -4, "Five", True, None, False, [1,2,[3,4,5],6], 10]
print(l4)
print(len(l4))
print(l4[-2])
# to fetch item from list which is in another list
print(l4[-2][2][2])