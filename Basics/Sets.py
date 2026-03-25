#sets are collection of items- non sequential and no indexing
#no slicing and no + operation
#set{}
set1 = {1, 2, 3, "Kiran", 2.5}
set2 = {4, 5, 6}
print(type(set1))
print(len(set1))

#sets do not allow duplicate values
set3 = {3,3,4,1,3.4}
print(set3)

#basic operations in set
#membership operator
print(3 in set3)

#no concatenation can not be done in sets
#need to convert it into another datatype.
#no repetition supported
print(set(tuple(set1) + tuple(set2)))

#add()
set3.add(5)
print(set3)

#remove()
set3.remove(1)
print(set3)


#add() add an element if it is already present
#no difference
set3.add(3)
print(set3)

#discard()
set3.discard(4)
print(set3)

#More operations on set
student1 = {"english", "maths", "punjabi", "computer"}
student2 = {"english", "maths", "Hindi", "computer"}
print(student1, student2)

#to find common subject of both students
#intersection
common_subejct= student1.intersection(student2)
print(common_subejct)
print(student1 & student2)

#union- to find all subjects either common or not
print(student1.union(student2))
print(student1 | student2)

#difference - elements in one set but not in another set
new= student2 - student1
print(new)

#Frozen set - Immutable sets
f1 = frozenset({1,3,5,8,0,12})
#make any set frozen so that we cannot make any changes