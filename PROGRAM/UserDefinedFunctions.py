#userdefined functions
#used for code reusing, modularity - logical
#function call
#function definition

s="python","html"
print(s.index("html")) #index is builtin function



def value_reverse(value):
    reverse = value[::-1]
    print(reverse)
s="python"
result = value_reverse(s)


l=[10,20,30,40,50]
result = value_reverse(l)
print(result)



#parameter passing techniues 

#positional argument
def linear_search(l,key):
    for value in l:
        if key==value:
            return True
    else:
        return False


l=[10,20,30,40,50]
key = 30
result = linear_search(l,key)
print(result)

#default argument 
#password genereator(char,upper,lower,special char,digits)
# print(ord('a'),ord('z'))
# print(ord('A'),ord('Z'))
# print(char(97))

import random
def gen_password(Length = 8):
    Upper = chr(random.randint(65,90))
    Lower = chr(random.randint(97,112))
    l = ['@','#','$']
    special = random.choice(l)
    digits = random.randint(10000,99999)

    password = Upper + Lower + special + str(digits)
    return password


result = gen_password()
print(result)


#keyword argument

#validating pasword somethoing
def validate(username,password):
    if username == "ABC" and password =="ABC@123":
        print("valid password")
    else:
        print("Invalid password")
validate("abc123","Abc@123")
validate("ABC","Abc@123")
validate("ABC","ABC@123")
validate(username="ABC",password="Abc@123")


#variable length positional argument

def add_value(*args):
    l = []
    for value in args:
        l.append(value)
    return l

result = add_value(10,20,30,40,50)
print(result)
result = add_value(10,20)
print(result)
result = add_value(10,20,30)
print(result)


#variable length keyword argument
#name, email,contact,dob

def get_details(**keywordargs):
    print(keywordargs)
result = get_details(name="abc",email="abc@gmail.com",contact="12345",dob="12-10-2002")
print(result)
result = get_details(name="abc",contact="12345",dob="12-10-2002")
print(result)
result = get_details(name="abc",email="abc@gmail.com",dob="12-10-2002")
print(result)


