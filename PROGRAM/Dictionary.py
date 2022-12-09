#Dictionary data type
#mutable, unoredered data structure, key should be unique 
#cant store duplicate key
#we can store only int float string tuple
d = {"hello_id":101,"name":"shubham","email":"abc@gmail.com","name":"date"}
print(d)
d = {"hello_id":101,"name":"shubham","email":"abc@gmail.com","name":"date",(10,20,30):1000}
print(d)


#add and update the elements
d["number"]=1234567
print(d)


#get and setdefault
print(d.get("name")) #tell us value of key
print(d.get("age","18+")) #since key not exist but we want to add and update answers


print(d.setdefault("name"))

print(d.setdefault("surname")) #since surname doesnot exist in list so it will add and return us none value
print(d)


#iterating
for x in d:
    print(x) # we will get keys 

for key in d: 
    print(key,d[key]) # we will get keys and its value


#for 1:1,2:4,3:9....10:100
d={}
for value in range(1,11):
    d[value] = value * value
print(d)

d={}
for value in range(1,11):
    d[value] = value * value
    print(d)


#keys,values,items
print(d.keys())
print(d.values())
print(d.items())


#update and delete 

# list into dictionary
l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
d=dict(zip(l1,l2))
print(d)

l=[1,2,3,4,5]
d = dict.fromkeys(l)
print(d)
d = dict.fromkeys(l,0)
print(d)


#merging to dictionary
l1={1:2,2:4,3:5,4:6,5:7}
l2={10:1,20:2,30:3,40:4,50:5}
l1.update(l2)
print(l1)


#delete
l1={1:2,2:4,3:5,4:6,5:7}
r =l1.pop(1)
print(l1,r)

l1={1:2,2:4,3:5,4:6,5:7}
r =l1.popitem() # picks randomy value
print(l1)

l1.clear()
print(l1)


