#input
a = int(input())
#output
print("Plan in order to print %s pages per month:" % a)
if a <=15:
    print("Free.")
    print("Price: 0 Euros.")
elif a <=50:
    print("Occasional.")
    print("Price: 2.99 Euros.")
elif a <=100:
    print("Moderate.")
    print("Price: 4.99 Euros.")
elif a<=300:
    print("Frequent.")
    print("Price: 9.99 Euros.")
elif a<=700:
    print("Business.")
    print("Price: 19.99 Euros.")
elif a>=700:
    print("Not available.")
    print("Price: - Euros.")