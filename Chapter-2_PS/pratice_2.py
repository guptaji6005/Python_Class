# QUE 1 - WAP to display user entered name followed by Good Afternoon using input() function

name = input("Enter your name:-")
print(f"Good Afternoon {name}")



# QUE 2 - WAP to fill in a letter template givrn brlow with name and date

letter = '''
        Dear <|Name|>,
        You are Selected!
        <|Date|>
        '''
print(letter.replace("<|Name|>","Abhinav").replace("<|Date|>","24 Sep 2024"))



# QUE 3 - WAP to detect double space in a space

name = "Abhinav is a good  boy and  "
print(name.find("  "))



# QUE 4 - WAP Replace the double space from problem 3 with single spaces

name = "Abhinav is a good  boy and  "
print(name.replace("  "," "))                          # String are immutable which mean that you cannot change them by running function on them


# QUE 5 - WAP to format the following letter using escape sequence character

letter = "Dear Abhhinav,\n\t This python course is nice.\nThanks!"
print(letter)