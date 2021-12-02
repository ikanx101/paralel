#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --time=168:00:00

cd $PWD

mpirun -np 24 --oversubscribe python3 job4.py
