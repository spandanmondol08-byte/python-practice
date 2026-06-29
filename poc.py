n= eval(input("Enter a list of numbers: "))
x=[]
for ch in n:
    c=len(str(ch))
    x.append(ch)
    x.append(c)
print(x)

