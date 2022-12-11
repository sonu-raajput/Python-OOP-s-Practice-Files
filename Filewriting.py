"""f = open ("Sonu.txt","rt")
content = f.readline()
print (content)
content = f.readline()
print(f.readline())
f.close()"""
f = open ("Sonu.txt")
for line in f:
    print(line,end="")
    content = f.read()
    print(content)

