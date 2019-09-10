def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

printme("Hello, Maycon Augusto!")
printme(str = "My String")

# Arguments required
def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return

printinfo("Maycon", 30)

# Keyword arguments
printinfo(name="Maycon", age=30)

# Default arguments
def printinfo(name, age=35):
    print("Name: ", name)
    print("Age ", age)
    return

printinfo("Maycon", 30)

# Variable length
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
