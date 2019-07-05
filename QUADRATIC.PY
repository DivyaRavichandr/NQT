from math import sqrt
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print((x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print( x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()
