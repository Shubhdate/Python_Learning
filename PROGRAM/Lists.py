#lists
#list are mutable - add update and delete
# list is ordered indexing and slicing
#store any types of data
#list copy on basis of memory location
l =[10,20,30,40, "hello","world",[100,200,300]]
print(l,type(l))

#indexing and slicing
l =[10,20,30,40, "hello","world",[100,200,300]]
print(l[-1][1])
print(l[1:3])


a = [10,20,30,40]
for value in l[:2]:
    print(value)


#append, extend, insert - to add element is list
a = [10,20,30,40]
a.append(600)
print(a)
a.extend([100,200,300,400])
print(a)
a.insert(1,1000)
print(a)

#update , delete method 
l=[10,20,30,40,50]
l[2] = 300
print(l)

#delete - pop, clear, remove del
l=[10,20,30,40,50]
r=l.pop()
print(l,r)
r=l.pop(2)
print(l,r)
r=l.remove(40)
print(l)
l.clear()
print(l)


l=[100,200,30,40,50]
l.sort()
print(l)
l.reverse()
print(l)
print(l.index(30))
print(l.count(30))


l=[100,200,30,40,50]
l2=[10,20,30,40,50]
print(l + l2)

l=0.1
print(l * 10)