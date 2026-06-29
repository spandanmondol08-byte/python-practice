p=int(input('Enter the lower limit : '))
q=int(input('Enter the upper limit : '))
for num in range(p,q+1):
    if num % 10 == 7 or num%7==0:
        print(num," is a buzz no. ")
    
