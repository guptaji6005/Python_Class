s = {1,5,7,32,54,5,5}
 
e = set()              # Don't use s = {} as it will create an enpty  dictionary

print(s)
print(type(s))

s.add(566)
print(s,type(s))
s.remove(1)
print(s,type(s))
s.pop()               # set element remove in the list