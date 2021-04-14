#input
a = list(input().lower())
isogram = True
#output
while len(a)>1:
    letter = a.pop(0)
    if letter in a:
        isogram = False
        break
if isogram:
    print ("Isogram detected")
else:
    print("Not an isogram")