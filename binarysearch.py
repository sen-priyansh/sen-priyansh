import random as r
d=list()
for i in range(100):
    d.append(r.randint(0,100))

print(d)

d.sort()
s=0
l=len(d)

print(d)

flag=False

x= int(input("Enter the element you want to find: "))

while s!=l:
    m = (s+l)//2

    if d[m]==x:
        print(m)
        flag=True
        break
    elif d[m]<x:
        s=m+1
    elif d[m]>x:
        l=m-1
print("The element you chose to found ",d[m]," is at in position ",m) if flag else print("Element not found")