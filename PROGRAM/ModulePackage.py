#module and packages
# import Recursive

# l=[10,20,30,40,50,60,70,80,90]
# key = 80
# result =  binary_search(l,key)
# print(result)

# help(Recursive)


#RE module Regx Meta-cahaecteristic Module - 
# import re
# . - any cahr
# [a-zA-Z] - cahr class
# [0-9] - digit class
# + - atleast one [a-z]+
# * - zero or more
# ^ - start of the 
# & - end of the 
# ? - optional
# [a-z]{2,4} - 

import re
s = "ABCDE1234A"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]&")
l = re.findall(r,s)
print(l)

#if phone number is valid or not
s = "0987654321"
r =re.compile("^[0-9]{9}&")
l = re.findall(r,s)
print(l)


#to check dd--mm-yyyy
s = "12-05-1022"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l = re.findall(r,s)
print(l)


#regular expression - GROUPS - useful for extracting data from the group ?p<> only for specicying
s = "12-05-2022"
r = re.compile("^(?P<Date>[0-9]{2})-(?P<Month>[0-9]{2})-(?P<year>[0-9]{4})$")
m = re.search(r,s)
if m:
    # print(m.group(1))
    print(m.group("year"))
else:
    print("pattern not found")
print(m.group())

#[0-9] \d
#[^0-9] \D

#[a-zA-Z0-9] \w
#\W

#space - \s
# \S