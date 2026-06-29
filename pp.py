n=5
k=1
for i in range(n):
    for j in range(i,n):
        print(' ' ,end='')
    p=k
    for j in range(i):
        print(p,end='')
        p=p-1
    m=1
    for j in range(i+1):
        print(m,end='')
        m=m+1
    k=k+1
    print()
n=5
k=5
for i in range(n):
    for j in range(i+1):
        print(' ' ,end='')
    p=k
    for j in range(i,n-1):
        print(p,end='')
        p=p-1
    m=1
    for j in range(i,n):
        print(m,end='')
        m=m+1
    k=k-1
    print()
        
