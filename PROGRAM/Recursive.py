#recursive - 
#factorial of numbers
def factorial(num):
    if num == 1: return 1
    else: return num * factorial(num - 1)

n1 = 5
result = factorial(n1)
print(result)


#binary search - to search something from the list by checking again and again
def binary_search(l,key):
    if len(l) ==0:
        return False
    else:
        mid = len(l) //2

        if l[mid] == key:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid],key)
        else: 
            return binary_search(l[mid+1:],key)

l=[10,20,30,40,50,60,70,80,90]
key = 90
result =  binary_search(l,key)
print(result)



#modules and packages
if __name__== '__main__':
    l=[10,20,30,40,50,60,70,80,90]
    key = 90
    result =  binary_search(l,key)
    print(result)