#Functional Programming - 
#map filter lamda are faster than ist compression

#map
def sqr(num1):
    return num1**2
l=[10,20,30,40,50]
result = list(map(sqr,l))
print(result)


def add(num1,num2):
    return num1+num2
l1=[10,20,30,40,50]
l2=[10,20,30,40,50,60,70]
result = list(map(add,l1,l2))
print(result)


#filter
def check_num(num1):
    if num1 % 2 ==0:
        return True
    else:
        return False
l=[10,20,30,40,50,60,70, 73,75,77]
result = list(filter(check_num,l))
print(result)


#lambda - use for only one function

l=[10,20,30,40,50]
result = list(map(lambda num1:num1**2,l))
print(result)


l=[10,20,30,40,50,60,70, 73,75,77]
result = list(filter(lambda num:num%2==0,l))
print(result)

