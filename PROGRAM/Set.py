#sets- - are mutable, all elements in the sets should be unique int,float tuple string can only be added

s ={10,20,30,40,50}
print(s)

#add elements
s ={10,20,30}
s.add(40)
print(s)

#update 
s1 ={10,20,30,40,60}
s2 ={10,20,30,40,50}
s3 = s1.union(s2)
print(s3)
s3 = s1.intersection(s2)
print(s3)
s3 = s1.difference(s2)
print(s3)
s3 = s1.symmetric_difference(s2)
print(s3)


s1.update(s2)
print(s1)
s1.intersection_update(s2)
print(s1)
s1.difference_update(s2)
print(s1)
s1.symmetric_difference(s2)
print(s1)


s1={10,20,30,40,50}
s2={10,20,30}
print(s2.issubset(s1))
print(s2.issuperset(s1))

#list into set
l = [10,20,30,40]
s = set(l)
print(s)


l1 = [10,20,30,40]
l2= [50,60,70,80,40,30,20,10]
s1 = set(l1)
s2 = set(l2)
s3 = s1.union(s2)
print(s3)
l3 = list(s3)
l3.sort()
print(l3)


#delete - pop , remove,discard,clear del

s={10,20,30,40,50,60}
r = s.pop() #random value
print(s,r)

s.remove(10)
print(s)

s.discard(20)
print(s)

s.clear()
print(s)