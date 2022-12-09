#strings are immutable, ordered data strcture-support indexing and slicing
s="python sample string"
print(type(s),id(s))

#indexing - from ltr to it is 1to infinity and right to left it is -1 to -infinity
s="python sample string"
print(s[-2])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
# print(s[40]) - #will tell us out of range


#slicing - 
k = "hello world"
print(k[0:5])
print(k[5:])
print(k[:8])


#stride - skips and print the values and alos direction of string
p = "hello world"
print(p[::2])
print(p[::3])
print(p[::-1])


#string built in data types - 

#format
n1=100
n2=200
print("value of n1 is", n1)
print("value of n2 is {}".format(n2))
print("value of n2 is {val2} value of n1 is {val1}".format(val1=n1,val2=n2))

#capitalize, upper,lower , title or checking it 
s =" hello world"
s = s.capitalize()
print(s)
s = s.upper()
print(s)
s = s.lower()
print(s)
s = s.title()
print(s)

s = s.title()
print(s.isupper())
s = s.title()
print(s.istitle())
#we dont have for capitalize


#split and join
s = "hello, world, python "
l = s.split(",")
print(l)
l = s.split(" ")
print(l)

s1 = (" ").join(l)
print(s1)
s1 = (",").join(l)
print(s1)


#maketrans, translate
a="1234"
b="abcd"
c="python is abcd"
table = str.maketrans(b,a)
result = c.translate(table)
print(result)


#index, find , rfind functiona="1234"
c="python ,python, python ,is, abcd"
print("python" in c)
print(c.index("python"))
print(c.rfind("python"))


#strip
s = "     this is sample string    "
s1 = s.strip(" ")
print(s1)
s = "&&&&&this is sample string&&&&&"
s1 = s.strip("&")
print(s1)


s = "python"
s1 = s.center(20, "&")
print(s1)


#replace
s = "hello world"
s1 = s.replace("world","king")
print(s1)