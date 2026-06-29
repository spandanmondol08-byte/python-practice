s="Nimda hay urebx fjgjjJJ 23jjKJH JDSF 13jdf"
z=u=l=d=sy=0
for a in s:
    if a.isspace():
        z+=1
    elif a.isupper():
        u+=1
    elif a.islower():
        l+=1
    elif a.isdigit():
        d+=1
    elif a.isalnum():
        sy+=1
c=s.split(' ')
p=len(c)
print(p,z,u,l,d,sy)
