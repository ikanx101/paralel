#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=720:00:00

export PATH=/opt/openmpi-3.1.4/build/bin:$PATH
export LD_LIBRARY_PATH=/opt/openmpi-3.1.4/build/lib:$LD_LIBRARY_PATH

mpirun -np 4 --oversubscribe python3 broad.py
