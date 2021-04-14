#input
a = input()
yarn = 0
sum = ""

while a !="#":
    sum += a
    a = input()
#output
for x in sum:
    if x == 'o':
        yarn += 1
    elif x == '+':
        yarn += 1.5
    elif x == 'T':
        yarn += 2
print(yarn)