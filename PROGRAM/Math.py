#sum
l=[10,20,30,40,50]
print(sum(l))
print(max(l))
print(min(l))

#roundoff
num=22.009
print(round(num))

#math module
import math
l=[0.1] * 10
print(l)
print(sum(l))

print(math.fsum(l))


#lowerbound and upperbound
num1= 15.9999
print(math.floor(15.9999),math.ceil(15.9999))


#squareroot
print(math.sqrt(20))
print(math.sqrt(399))

#factorial
print(math.factorial(5))
print(math.factorial(34))

num1=45.999
print(math.modf(num1))


#power
print(math.pow(10,2))
print(math.pow(19,2))


#log
print(math.log(10)) #base to e
print(math.log10(34))
print(math.log2(34))

#trignometric
print(math.sin(30)) #degrees
print(math.sin(math.radians(30)))
print(math.cos(30)) 
print(math.tan(30)) 

#will get all math operation but right import math
# help(math)
# print(dir(math))


#random
import random
# print(random.random())
l=[1,2,3,4,5,6]
print(random.choice(l))
print(random.randint(1,3))
print(random.randrange(1,3))