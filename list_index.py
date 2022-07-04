m=[23,4,87,17,629]
n=int(input("Enter number of list element: "))
if n<len(m):
    print(m[n])
    print(m[-n])
print(m[:-2:2])
n=float(input("Enter number to search in list: "))
if n in m:
    print("%d is in list" %n)
else:
    print("%d is not in list" %n)
print(len("Hello, World"))
n=input("Enter symbol to search: ")
if n in "Hello, World":
    print("%s is in string" %n)
else:
    print("%s is not in string" %n)
n= "Hello, World"
print(n[::-1])
print(n[7:10:1]+n[-1])