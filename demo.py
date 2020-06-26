digits = 0
letters = 0
st = input("Enter the string: ")
for i in st:
    if (i.isdigit()):
        digits = digits+1
letters = len(st)-digits
print("Digits: ",digits,"Letters: ",letters)

