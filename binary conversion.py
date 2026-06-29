def bin_dec(n):
    l=len(str(n))
    s=0
    for i in range(l):
        a=n%10
        s=s+a*(2)**i
        n=n//10
    return s

    
