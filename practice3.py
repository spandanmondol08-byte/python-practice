n=7
for i in range(n):
    for j in range(4):
        if (j==0)or (i+j==6) or (i==j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
