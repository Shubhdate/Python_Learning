#int
num1=100
print(type(num1))


#float - to store deimal numbers
num2=10.000001
print(type(num2))


#string - for "" '' """ """
s = "python"
print(s, type(s))
q = 'python'
print(s, type(s))
q = 'python "king"'
print(s, type(s))


#list - to add multiple values ie enclosed in square bracket 
l = [10,20,30,40, "king", "hello","world"]
print(type(l))
l.append("to add new element in list if we forgot to add")
print(l)


#tuple - store datatypes enclosed in breackets but we cannot add, delete, move that 
t = (10,20,30,"shubham")
print(t)

#dicitonary - stores values as format of key or paswords enclosed in curly bracket
d = {"NAME":"SHUBHAM DATE"}
print(d)

#set
set = {10,20,30}
print(set)

#boolean - true or false
b = True
print(b)
b = False
print(b)


#complex - for complex number
c = 7 + 9j
print(c)

