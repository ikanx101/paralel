import timeit
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def y(x):
    return(x**2)
def trapezoidal(a,b,n):
    h = (b-a)/n
    s = (y(a)+y(b))
    i=1
    while i<n:
        s+=2*y(a+i*h)
        i+=1
    return((h/2)*s)
a=0
b=1
n= 10 ** 9
dest=0
h=(b-a)/n
local_n=n/size
local_a=a+rank*local_n*h
local_b=local_a+local_n*h

t1 = MPI.Wtime()
s=trapezoidal(local_a, local_b, local_n)    

if rank ==0:
    total=s
    for _ in range(size-1):
        total2 = comm.recv(source = MPI.ANY_SOURCE)
        total += total2
    print("integral ", total)
    print("time= ", MPI.Wtime()-t1)
else:
    comm.send(s,dest=0)