#Tuple
#(item1, item2,....)

t1= ("Python", 10, 2.3, -1, True, None, [1,2,3,4], (10,20))
print(t1)
print(len(t1))
print(t1[-2])
print(t1[0:8:2])
print(type(t1))

l1 = [1,2,3]
print(tuple(l1))

#Basic Operations on Tuples
t2 = ("Kiran", 25, "Female")
t3= t2+t1
print(t3)

#*
print(t2 * 2)

#in and not in
print("Female" in t3)
print("Female" in t1)

#count
print(t3.count("Female"))

#index
print(t1.index(-1))

#min/max
t4= (1,2,3,4,5)
print(min(t4))
print(max(t4))
print(id(t4))
