#List Comprehension - can be performed in list, tuple, dictionary or on same set of eleemnts
l=[10,20,30,40,50]
l2=[]
for value in l:
    l2.append(value * value)
print(l2)

#method 2
l=[10,20,30,40,50]
l2=[value * value for value in l]
print(l2)

l=[10,20,30,40,50,60,70,80]
l2=[value for value in l if value%2 == 0]
print(l2)


l=["abc","abcd","abcde"]
l2=[len(value) for value in l]
print(l2)


l2=[(value1,value2) for value1 in range(1,5) for value2 in range (100,105)]
print(l2)


l=[[1,2],[3,4,5],[6,7,8,9]]
l2=[]
for value in l:
    for val2 in value:
        l2.append(val2)
print(l2)

l=[[1,2],[3,4,5],[6,7,8,9]]
l2 = [val2 for value in l for val2 in value]
print(l2)
# l2=[1,2,3,4] output


l=[100,105,110,115,120]
l2=["even" if value%2 ==0 else "odd" for value in l]
print(l2)