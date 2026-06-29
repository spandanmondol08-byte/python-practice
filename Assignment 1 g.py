r1=float(input("Enter the Resistance of the first resister in Ohms: "))
r2=float(input("Enter the Resistance of the second resister in Ohms: "))
s=r1+r2
p=(1/r1)+(1/r2)
print("The equivalent resistance of the resistors in series is: ",s)
print("The equivalent resistance of the resistors in parallel is: ",p,"Ohms")
