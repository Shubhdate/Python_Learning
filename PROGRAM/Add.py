first_num = 10
second_num = 55
add = first_num + second_num
print(add)

print(type(first_num), type(second_num))
# above is used to find out what is variable datatype

print(id(first_num), id(second_num))
# above is used for telling us memory loaction of variable where it is stored

a=10
b=10
print(id(a), id(b))
#here both the value are same so loaction will be also same which is called as object intering


#if we want to know in detail we can write help(name of datatype)
help(str)