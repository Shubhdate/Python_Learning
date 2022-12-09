#Iterators nad Itertools - faster than lists
l=[100,200,300,400,500]
i = iter(l)
print(i)
print(next(i))
print(next(i))

#convert to iters
import itertools
l1=[10,20,30,40,50,60]
l2=[100,200,300,400,500]
l3=[1000,2000,3000,4000,5000]
i = itertools.chain(l1,l2,l3)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


l1=[10,20,30,40,50,60]
count = 0
for value in itertools.cycle(l1):
    if count < 20:
        print(value)
    else:
        break
    count+=1


l1=[10,20,30,40,50,60]
count = 0
for value in itertools.repeat(l1):
    if count < 20:
        print(value)
    else:
        break
    count+=1


l=[10,20,30,40,50,60]
i = iter(l)
t = itertools.tee(i)
print(t)
for value in t[0]:
    print(value)
for value in t[1]:
    print(value)


l=[1,2,3,4,5,6]
print(list(itertools.permutations(l,2)))
print(list(itertools.combinations(l,2)))
print(list(itertools.combinations_with_replacement(l,2)))

