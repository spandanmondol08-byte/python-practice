a = int(input("Enter the coefficient of x^2: "))
if a == 0:
    print("Please enter a valid coefficient")
else:
    b = int(input("Enter the coefficient of x: "))
    c = int(input("Enter the constant: "))
    d = (b**2) - (4*a*c)
    e = (-b + (d**0.5)) / (2*a)
    f = (-b - (d**0.5)) / (2*a)
    print ("The roots of the equation are", e , f)
