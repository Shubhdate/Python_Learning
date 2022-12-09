#Arithemetic operators - + - * % / // **
n1=10
n2=23
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(n1**n2)
print(n1%n2)

#Comparison operators - to compare values datatypes ie strings numbers lists dictionary etc < > <= >= == != if right then gives true else gives false
n1=100
n2=200
print(n1>n2)
print(n1<n2)
print(n1>+n2)
print(n1<=n2)
print(n1==n2)
print(n1!=n2)

#identity operators - compare the memeory loaction of datatypes and gives answer on that reason is(true) isnot(false)
n1=100
n2=100
print(n1 is n2)
print(n1 is not n2)

l=[10,20,30]
l2=[10,20,0]
print(l==12)
print(l2 is 12)
print(l2 is not 12)

#Assignment Operators - =, +=, -=, *=, /=
n1=100
# n1= n1 + 100
# print(n1)

n1 += 100
print(n1)
n1 -= 100
print(n1)
n1 /= 100
print(n1)
n1 *= 100
print(n1)

#bitwise operators - for shifting & | ^ >> <<
n1=2
n2=1
print(bin(n1), bin(n2))
print(n1 & n2)
print(n1 | n2)
print(n1 ^ n2)
print(n1 >> n2)
print(n1 << n2)

#logical operators - and ,or, not
print(10==10 and 20==10)
print(10==10 or 20==10)
print(not(10==10))
print(not(10==20))

#memebership operators - for checking or searching something in word integers or in data types and gives true or false answers
l=[10,20,30,40,50]
print(30 in l)
print(30 not in l)

print(60 in l)
print(60 not in l)

