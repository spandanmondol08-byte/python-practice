n=input('Enter your name: ')
a=input('Enter your address: ')
p=int(input('Enter your premium amount: '))
t=int(input('Enter your no. of years: '))
r=input('Enter the ploicy opted (C for child / N for normal plan): ')
if p < 5000:
    print('Minimum amount must be 5000')
else:
    if p==5000 and r=='C':
        rate=3
    elif p==5000 and r=='N':
        rate=1.5
    elif p>5000 and p<=20000 and r=='C':
        rate=5
    elif p>5000 and p<=20000 and r=='N':
        rate=3.5
    elif p>20000 and p<=45000 and r=='C':
        rate=7
    elif p>5000 and p<=45000 and r=='N':
        rate=6
    elif p>45000 and r=='C':
        rate=10
    elif p>45000 and r=='N':
        rate=8.5
bonus1=(rate/100)*p
bonus=bonus1*t
M=p+bonus
print("Bonus for 1 year: ",bonus1,)
print("Bonus for"  ,t, "year: ",bonus,)
print('Maturity amount',M)
