def analyse(L):
    s=L.split(' ')
    a=['a','e','i','o','u']
    t=()
    for ch in s:
        l=len(ch)
        f=ch[0] in a
        if l==6 and f is True:
            t=t+(ch,)
    print(t)
p=analyse('I am Spandan broo actors becher either')
