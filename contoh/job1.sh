#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=168:00:00

cd $PWD

mpirun -np 4 --oversubscribe python3 job1.py
