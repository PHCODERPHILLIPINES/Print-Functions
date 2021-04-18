"""
    This activity shows the 5 basic methods of how to use the print statement
    and add variable value.
"""
# Option 1: The basic print function
print("Hello audience!")
# Option 2: Using the , or + separators to add variable values
# Declaration of variables
name = "PHCoder"
description = 'hit that like and subscribe button!'
# Using ','
print("My name is", name,"!")
# Using '+'
print("Please " + description)

# Option 3: Using the f-string function
# Declare
name = 'John'
age = 34
# application
print(f"{name} is {age} years old!")
# Option 4: .format method
# Declare
favorite = 'pizzas'
# application
print("{} likes {}.".format(name, favorite))
# Option 5: % formatting method
# Remember to visit the website that I placed in the description to know what to place
# Declare
wishes = 3
# application
print("If I had %d wishes, I'll ask for %d more %s!" % (wishes, wishes, favorite))
# Extra Technique: For adding a new line there are 2 basic ways

# Technique 1: blank print function
print("")
print("I created it by using a empty print function")
# Technique 2: using \n function
print("\nThis is my recommendation for it keeps your code short!")

"""
 Bye Bye!   
"""