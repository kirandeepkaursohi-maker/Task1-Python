#Dictionaries- key value pairs {}
#D1 = {key1:value1, key2:value2,...}

d1 = {"milk":60, "rice": 80, "bread":20}
print(d1)
print(type(d1))

#lenght gives 1 pair 1 count. not pair as 2 count
print(len(d1))

#to convert it into another data type
print(list(d1.keys()))
print(list(d1.values()))

#to check value store for any key
print(d1["milk"])

#dictionary are mutable
#to replace value
d1["milk"] = 30
print(d1)

#too add new key value pair
d1["eggs"] = 40
print(d1)

#operations in dict
#updating and deleting
d2= {"M":10, "B":20, "C":30}
print(d2)
#fetch marks for C- gives error when key is not present
print(d2["C"])

#get() - no error even when key is not present
print(d2.get("C"))
#to update marks
print(d2.get("ID"), 40) #not saved permanently
print(d2)

#membership operator
print("C" in d2)
print(10 in d2)

#update()
d1.update(d2)
print(d1)

#deleting pop()
d2.pop("C")
print(d2)

#if we have two same keys but different values
#while creating dict it reads left to right
#only one key will get added and value will be the last value entered in the dict

#working with keys and values
#not allowed: mutable: list, set , dict
#allowed: immutable: tuples; strings, integers, float, boolean

#shallow copy and deep copy
import copy
l1 = [1,2,[10,20,20], "python"]

#shallow copy
'''
l2 = copy.copy(l1)
print(l2)

print(id(l1))
print(id(l2))
l1[2][0] = 100 # change in both
l1[0] = 100  #only change in l1
print(l1)
print(l2)
'''
#deepcopy
l2 = copy.deepcopy(l1)
l1[2][0] = 100 # change in both
l1[0] = 100
print(l1)
print(l2)