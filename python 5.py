n=int(input('Enter: '))
x=n
s=0
while n!=0:
    rev=1
    rem=n%10
    for i in range(1,rem+1):
        rev=rev*i
    s=s+rev
    n=n//10
if s-x==0:
    print("yes")
else:
    print('no')
    

