t=()
s1=0
s2=0
p=1
print('Enter 10 integers')
for i in range(0,10):
    x=int(input())
    t=t+(x,)
print(t)
for f in t:
    if f%2==0:
        s2=s2+f
        p=p*f
    else:
        s1=s1+f
a=(s1+s2)/2
print('Average of nos.',a)
print('Sum of odd no.',s1)
print('Product of even no.',p)
