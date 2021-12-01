from mpi4py import MPI
import time

start=time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



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

a=0
b=1
n=10000
h=(b-a)/n
local_n=n/size
i=1
local_a=[0 for i in range(4)]
local_b=[0 for i in range(4)]
if rank == 0:
    for i in range(size):
        local_a[i]=a+rank*local_n*h
        local_b[i]=local_a[i]+local_n*h
    data = [(local_a[i],local_b[i]) for i in range(size)]
else:
    data = None

data=comm.scatter(data,root=0)

s=trapezoidal(a,b,n)
total=s

if rank==0:
    print("integral=", total)
    print("time=", time.time()-start)

