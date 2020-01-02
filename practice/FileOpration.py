
# Read file function
def rd():

    # Open file read mode
    r=open("test.txt",'r')
    print(r.read())
    r.close()

# Open file Write mode
f= open("test.txt",'w')
f.write("Hello This Is Test File And it's open write mode")
f.close()

# Open file append mode
a=open("test.txt",'a')
a.write("/nThis is Append Content")
rd()
