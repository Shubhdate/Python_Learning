#Generator Function - used to save memory in python

def printVal(l):
    for value in l:
        print(value)
l=[10,20,30,40,50,60,70]
printVal(l)

#fibonnaci series
def fibo():
    first_num = 0
    second_num = 1
    yield second_num
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num, second_num = second_num, next_val

g = fibo()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for value in range(20):
    print(next(g))
