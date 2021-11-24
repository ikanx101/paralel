import timeit
import numpy as np
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

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
n = [1,7,16,28,36,43,52,62,69,77,93,322,359,3620,4374,4513,5575,6680,7455,9334,9533,227373,235875,359596,441394,611944,651434,707928,756462,914272,947220,1911445,3542919,4448887,33173155,33744249,53990692,60063717,60461719,68180038,72434461,74711604,76351391,80842245,89589529,90095249,90814922,92609483,95720398,96263304,97769854,217967736,314781656,356988524,719449697,862513064,1000000000]
integral = []
waktu = []

for i in range(0,len(n)):
  dest=0
  h=(b-a)/n[i]
  local_n=n[i]/size
  local_a=a+rank*local_n*h
  local_b=local_a+local_n*h

  print(i)

  t1 = MPI.Wtime()
  s=trapezoidal(local_a,local_b,local_n)

  if rank==0:
      total=s
      for _ in range(size-1):
          total2 = comm.recv(source = MPI.ANY_SOURCE)
          total += total2
      integral.append(total)
      waktu.append(MPI.Wtime()-t1)
  else:
      comm.send(s,dest=0)

f = open("paralel.csv","w+")
f.write("n,integral,waktu\n")
for j in range(0,len(n)) :
  f.write(str(n[j])+","+str(integral[j])+","+str(waktu[j])+"\n")
f.close()

print("DONE")
