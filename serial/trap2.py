import time
import numpy as np

def y(x):
    return x**2

def trapezoidal(a,b,n):
    h=(b-a)/n
    s=(y(a)+y(b))
    i=1
    for i in range (1,n):
          s+=2*y(a+i*h)
          i+=1
    return((h/2)*s)

x0 = 0
xn = 1
n = [1,7,16,28,36,43,52,62,69,77,93,322,359,3620,4374,4513,5575,6680,7455,9334,9533,227373,235875,359596,441394,611944,651434,707928,756462,914272,947220,1911445,3542919,4448887,33173155,33744249,53990692,60063717,60461719,68180038,72434461,74711604,76351391,80842245,89589529,90095249,90814922,92609483,95720398,96263304,97769854,217967736,314781656,356988524,719449697,862513064,1000000000]

n_selang = []
integral = []
waktu = []

for i in range(0,len(n)):
  start=time.time()
  t_1 = trapezoidal(x0,xn,n[i])
  end = time.time()
  t_2 = end - start
  n_selang.append(n[i])
  integral.append(t_1)
  waktu.append(t_2)

f = open("serial.csv","w+")
f.write("n,integral,waktu\n")
for j in range(0,len(n)) :
  f.write(str(n[j])+","+str(integral[j])+","+str(waktu[j])+"\n")
f.close()

print("DONE")
