f = open("SOONU.txt","a")
a= f.write("Sonu is nice guy")
print (a)
f.close()

""" Handle read and write """
f = open("Sonu.txt", "r+")
print(f.read())
f.write("Thank you")
f.close()
