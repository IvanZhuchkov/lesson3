n=int(input("Enter factorial: "))
m=[1]
for i in range(n):
    m.append(m[i]*(i+1)) 
del m[0]
print(m)