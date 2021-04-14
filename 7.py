#input
a = int(input())
b = int(input())
c = int(input())
#output
if a+b>c and a+c>b and c+b>a:
    print("It is a triangle")
else:
    print("It is NOT a triangle")
