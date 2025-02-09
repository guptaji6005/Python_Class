# A spam comment is defined as a text containing following keywords:
#"Make a lot of money","buy now","subscribe this","click me". Write a program to detect these spams.


p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = "Subscribe this"
p4 = "Click Me"

message = input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or(p4 in message)):
    print("This is a spam")
else:
    print("This comment is not a spam")