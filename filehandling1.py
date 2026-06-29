def add():
    f=open('text.txt','a')
    x=input('Enter the data: ')
    f1=f.write(x)
    print('Done')
    f.close()
def show():
    f=open('text.txt','r')
    f1=f.read()
    print(f1)
    f.close()
def count():
    f=open('text.txt','r')
    f1=f.read()
    s=v=c=d=0
    for i  in f1:
        if i.isspace()==True:
            s=s+1
        if i.isalpha()==True:
            if i in ['a','e','i','o','u','A','E','I','U','O']:
                v=v+1
            else:
                c=c+1
        if i.isdigit():
            d=d+1
    f2=f1.split()
    w=len(f2)
    print('Space:',s)
    print('Vowel:',v)
    print('Digits:',d)
    print('Consonant:',c)
    print('Words:',w)
    f.close()
def search():
    sw=input('Enter the Word to Search: ')
    f=open('text.txt','r')
    f1=f.read()
    f2=f1.split()
    for i in f2:
        if sw==i:
            print('FOUND!!')
    f.close()
def display():
    f=open('text.txt','r')
    f1=f.read()
    s=len(f1)
    f.seek(0)
    f2=f.readlines()
    l=len(f2)
    print('Size:',s)
    print('Length:',l)
while True:
    c=int(input('Enter your choice: '))
    if c==1:
        add()
    if c==2:
        show()
    if c==3:
        count()
    if c==4:
        search()
    if c==5:
        display()
    if c==6:
        break
