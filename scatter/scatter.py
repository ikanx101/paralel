from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

if rank == 0:
    data = np.arange(15.0)
    # menentukan size dari setiap sub-task​
    ave, res = divmod(data.size, nprocs)
    counts = [ave + 1 if p < res else ave for p in range(nprocs)]
    # menentukan indeks awal dan akhir dari setiap sub-task​
    starts = [sum(counts[:p]) for p in range(nprocs)]
    ends = [sum(counts[:p+1]) for p in range(nprocs)]
    # mengubah data menjadi list array ​
    data = [data[starts[p]:ends[p]] for p in range(nprocs)]
else:
    data = None

data = comm.scatter(data, root=0)
print('Process {} has data:'.format(rank), data)
