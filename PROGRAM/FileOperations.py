#File Operations
# r = read r+
# w = write w+
# a = append a+


#READ
# fp = open("javaprogram.txt","r")
# content = fp.read()
# print(content)


# #to read specify caharcters
# fp = open("javaprogram.txt","r")
# content = fp.read(20)
# print(content)

# #readlines and readline
# fp = open("javaprogram.txt","r")
# content = fp.readlines()
# print(content)

# fp = open("javaprogram.txt","r")
# content = fp.readlines()
# print(content[:10])

# fp = open("javaprogram.txt","r")
# content = fp.readline()
# print(content)


#WRITE - it will delete all content
#WE CANNOT PERFORM READ OPERATION IN IT

fp = open("input.txt","w")
content = fp.write("write this line to a file")
print(content)

fp = open("input.txt","w")
content = fp.write("hello")
print(content)

#tell and seek
#tell will help us to finnd current file position
#seek will help us to change the file position
# offset = number of charcter
# position - 0(start of the file) 1(current position) 2(end of the File )
# eg. seek(15,0) - change the fp by 15 char from start of the file )
#eg.seek(0,2) - change the fp by 0 cahr from end of the file

#w+ - write + read - we cannot get our old content but we can write new content

fp = open("input.txt","w+")
print(fp.tell())
fp.write("king is back")
print(fp.tell())
fp.seek(0,0)
print(fp.tell())
content = fp.read()
print(fp.tell())
print(content)


#r+ - read+write - maintain the old content and also we can write new content
fp = open("input.txt","r+")
content = fp.read()
print(content)
fp.write("\n\n sample line is added using python script")


# a and a+ - fp is at end
# a - only write
# a+ - both read and write operation
fp = open("input.txt","a+")
print(fp.tell())
content = fp.read()
print(content)


# r - fp -start, file should already present, read
# r+ - fp - start, file should already present, read + write

# w - fp - strat, create a new file, write
# w+ - fp - start, create a new file , write =  read

# a - fp - end, create a new file, write at the End 
# a+ - fp - end, create a new file , write + read