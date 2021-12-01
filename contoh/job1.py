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

if rank==0:
    n=1000000000
else:
    n=0


n=comm.bcast(n,root=0)

s=trapezoidal(a,b,n)
total=s


if rank==0:
    print("integral=", total)
    print("time=", time.time()-start)

