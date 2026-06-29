l=float(input("Enter the lenght of the cuboid: "))
b=float(input("Enter the breadth of the cuboid: "))
h=float(input("Enter the height of the cuboid: "))
d=(l**2 + b**2 + h**2)**0.5
a=2*(l*b + b*h + h*l)
v=l*b*h
print("The lenght of diagonal of the cuboid is: ",d)
print("The total surface area of the cuboid is: ",a)
print("The volume of the cuboid is: ",v)
