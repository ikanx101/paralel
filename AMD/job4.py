from mpi4py import MPI
import time

start = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def y(x):
    return x ** 2


def trapezoidal(a, b, n):
    h = (b - a) / n
    s = (y(a) + y(b))
    i = 1
    while i < n:
        s += 2 * y(a + i * h)
        i += 1
    return ((h / 2) * s)


a = 0
b = 1
n = 10 ** 9
h = (b - a) / n
local_n = n / size
local_a = a + rank * local_n * h
local_b = local_a + local_n * h
s = trapezoidal(local_a, local_b, local_n)
total = s

total = comm.reduce(total, op=MPI.SUM, root=0)

if rank == 0:
    print(f"n={n}, reduce")
    print("integral=", total)
    print("time=", time.time() - start)