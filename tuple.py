s=[1,2,2,3,3,3,3,4,4,5,6]
d={}
for i in s:
    key=i
    if key not in d:
        c=s.count(i)
        d[key]=c
print(d)
        
