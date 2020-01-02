# 1. WAP To print "Hello World".
# print("Hello World")

# 2. WAP To arithmetic operations.
n1=1
n2=2
# print(n1+n2)

# 3. WAP To Get Value from The user and perform arithmetic operation
# n1=int(input("Enter First number : "))
# n2=int(input("Enter Second number : "))
# print(n1+n2)

# 4. WAP To Create List.
name = ["Hardik","Manish""Ketan","Parth","Raj","Vatsal","Praful"]
# print(name)

# 5. Create Simple list and Add value , Slice the value , remove Specific value ,Clear List (using it's function).

# Create and copy list
name_list = ["Hardik","Manish","Ketan","Parth","Raj","Vatsal","Praful"]
nm=name_list.copy()
# print(nm)

# Add Value in list
nm.append("Arjun")
# print(nm)

# Slice the value in list
bnm=nm[0:3]
# print(bnm)

# remove Specific value in list
nm.remove("Praful")
# print(nm)

# Clear List
nm.clear()
# print(nm)

# 6. WAP to Create SET.
prbln={"Java","Python","Android","Sql"}
# print(name_set)

# 7. Create Simple set and Add value , remove Specific value(using discard and remove both function) ,Clear Set (using it's
# function).

# Create and copy list
prbln_set={"Java","Python","Android","Sql"}
ps=prbln_set.copy()
# print(ps)
ps.add("Php")
# print(ps)

# remove Specific value
ps.discard("Sql")
ps.remove("Android")
# print(ps)