d = {}     # empty dict

marks = {
    "Archit" : 100,
    "Pranav" : 98,
    "Rohan" : 23,
    0:"Rajendra"
}

print(marks, " -> ",type(marks))
print(marks["Pranav"])

print(marks.items())        # KIsme kya store hai wo btayega

print(marks.keys())         # main key dega jo value sote kr ke rkha hai 

print(marks.values())       # Only value return krega

marks.update({"Archit":99,"Renuka":72})          # update the entire dicsconry
print(marks)

print(marks.get("Archit2"))           # print none
print(marks["Archit2"])            # its return error