#-----Arithmetic Operator------#

a = 7
b = 4
c = a+b
print(c)

#------Assignment Operator------#

a = 4-2
print(a)
b = 6
# b += 3         # Increment the value of b by 3 and then assign it to b
print(b)
b -= 3           # Decrement the value of b by 3 and then assign it to b
print(b)



#------Comparision Operator------#
d = 5!=7                   # comparision operator also return in bolean velue True/False
print(d)                  # ==, >, <, =>, =<, != etc




#------Logical Operator------#

# True and True is return True
# True or False is return True

e = True or False
# Truth Table of 'or'
print("True or False is:-",True or False)
print("True or True is:-",True or True)
print("False or True is:-",False or True)
print("False or False is:-",False or False)

# Truth Table of 'and'
print("True and False is:-",True and False)
print("True and True is:-",True and True)
print("False and True is:-",False and True)
print("False and False is:-",False and False)

# Truth Table of 'not'
print(not(True))