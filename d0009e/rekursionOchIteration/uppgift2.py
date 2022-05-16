import math

def derivative(f,x,h):
    result = 1/(2*h)*((f(x+h))-(f(x-h)))
    return (result)

def solve(f, x0, h):
    x = 0
    while True:
        x = x0 - ((f(x0))/derivative(f, x0, h))
        if abs(x - x0) < h:
            return x
        x0 = x
        print(x)

#print(derivative(math.cos,3,0.001))
#solve(math.cos, 0.4, 0.0001)