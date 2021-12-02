import time

start=time.time()

def y(x):
    return x**2

def trapezoidal(a,b,n):
    h=(b-a)/n
    s=(y(a)+y(b))
    i=1
    while i<n:
        s+=2*y(a+i*h)
        i+=1
    return((h/2)*s)
x0=0
xn=1
n=10**9
print("integral: ", trapezoidal(x0,xn,n))

end=time.time()
print(end-start)
