n=input()
s=''
for i in n:
    if 'a'<= i <= 'z':
       s=s+chr(ord(i)-32)
    else:
        s=s+i
print(s)
