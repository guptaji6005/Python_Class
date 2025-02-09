# WAP to find out whether a given post is talking about "Abhinav" or not?

post = input("Enter the post:")

if("Abhinav".lower() in post.lower()):
    print("This post is talking about Abhinav")

else:
    print("This post is not talking about Abhinav")