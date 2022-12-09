#Tuple
#immutable data structure
#oredered indexing and slicing

t=(10,20,30,40,50)
print(t.index(20))
print(t.count(20))


t=(10,20,30,40,50)
for t in enumerate(t):
    print(t)

# list into tuple
l=[10,20,30,40,50]
t = tuple(l)
print(t)

t=("a","b","c","d")
l=list(t)
print(l)