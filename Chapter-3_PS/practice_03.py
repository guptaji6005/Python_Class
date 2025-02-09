# Que 1 - WAP to store sevent fruit in a list enter by the user?

fruits = [] 
f1 = input("Enter fruit name:")
fruits.append(f1)
f2 = input("Enter fruit name:")
fruits.append(f2)
f3 = input("Enter fruit name:")
fruits.append(f3)
f4 = input("Enter fruit name:")
fruits.append(f4)
f5 = input("Enter fruit name:")
fruits.append(f5)

print(fruits)



# Que 2 - WAP to accept marks of 6 student and displey them in a sorted manner?

marks = [] 
f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here: "))
marks.append(f5)
marks.sort()
print(marks)



# Que 3 - Check a tuple cannot be change in python?

a = (34,234,"Abhinav")
a[2] = "Archit"



# Que 4 - WAP to sum list with 4 numbers?

l1 = [4,3,6,1]
print(sum(l1))


# Que 5 - WAP to count a number of zero in the following tuple?

a = (7,0,8,0,0,9)
b = a.count(0)
print(b)