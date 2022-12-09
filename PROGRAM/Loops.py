#for loops - preffer to check something in range or values
# for [variable_name] in [iterable datatype]:
#     statements
#iterable data types - string, list, tuple, set
l=[10,20,30,40,50]
sum = 0
for value in l:
    sum = sum + value
    print(sum)
#this will give output 10 30 60 100 150

# range(5) - 0 1 2 3 4 will give us range
# range(10,15) - 10 11 12 13 14 
# range(10,20,2) - 10 12 14 16 18 

for value in range(5): print(value)
for value in range(10,15): print(value)
for value in range(10,20,2): print(value)

sum = 0
for value in range(1,10): 
    sum = sum + value 
print(sum)
# gives us last total answers

#iterating using for loop \continue\break\enumerate
l=[10,20,30,40,50,60]
key = 40
for value in l:
    if value == key:
        print("element found")
        break
    else:
        continue
else:
    print("element not found")
print("statement after the for loop")



l=[10,20,30,40,50,60]
key = 40
for index,value in enumerate(l):
    if value == key:
        print("element found at index", index)
        break
    else:
        continue
else:
    print("element not found")
print("statement after the for loop")


l=[10,20,30,40,50,60]
key = 400
for index,value in enumerate(l):
    if value == key:
        print("element found at index", index)
        break
    else:
        pass
        print("not found")
else:
    print("element not found")
print("statement after the for loop")



#while loop - preffer to check some condition
# while[condition]:
#     [statements]
# else:


#to find 1-20 number
count = 1
summ = 0
while count <=20:
    sum = sum + count
    count = count + 1
print(sum)
