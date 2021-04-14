#input
a = [int(x) for x in input().split(' ')]
a += [int(x) for x in input().split(' ')]
a += [int(x) for x in input().split(' ')]
#output
missing = []
for n in range(1, 10):
    if n not in a:
        missing.append(n)
if not missing:
    print("This is a valid sudoku")
else:
    print("This is an invalid sudoku. Missing numbers are:")
    for n in missing:
        print(n)