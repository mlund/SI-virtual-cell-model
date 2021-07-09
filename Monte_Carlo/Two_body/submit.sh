#!/bin/bash
#SBATCH -A lu2021-2-39
#SBATCH -N 1
#SBATCH --tasks-per-node=1
#SBATCH --mem-per-cpu=100
#SBATCH -t 168:00:00

#SBATCH -J MC_TB
#SBATCH -o out
#SBATCH -e err


module purge
module load foss

cd $SLURM_SUBMIT_DIR
OMP_NUM_THREADS=1;/home/marpoli/Work/faunus_master/faunus -i input.json  > out

