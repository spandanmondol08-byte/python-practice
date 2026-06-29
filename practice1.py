import math as m
n=int(input('Enter the no. n: '))
x=int(input('Enter the no. x: '))
s=x
a=2
b=2
for i in range(2,n+1):
    f=1
    if i%2==0:
        for j in range(1,b+1):
            f=f*j
        s+=(x**a)/f
    else:
        for j in range(1,b+1):
            f=f*j
        s-=(x**a)/f
    a=a+1
    b+=1
print(s)
