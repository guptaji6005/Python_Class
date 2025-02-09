a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entring an invalid negative age")

elif(a==0):
    print("You are entring 0 which is not a valid age")

else:
    print("You are below the age of content")

print("End of the program")