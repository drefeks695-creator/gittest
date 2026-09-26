from math import sqrt

x = -10
y = -5
while x <= 10 and y <= 5:
    S = x**2 + y**2
    xa = round(x)
    Sa= round(S)
    ya= round(y)
    print(f"{xa} {ya} {Sa}")
    y = y + 0.5    
    x = x + 0.2
   