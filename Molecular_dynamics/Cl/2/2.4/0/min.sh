#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres=gpu:2
#SBATCH --mem-per-cpu=500
#SBATCH -N 1
#SBATCH -A ...
#SBACTH --tasks-per-node=10
#SBACTH -n 10

#
# job time, change for what your job requires
#SBATCH -t 01:00:00
#
# job name
#SBATCH -J Cl_m
#
# filenames stdout and stderr - customise, include %j
#SBATCH -e min_err
#SBATCH -o min_out

cd $SLURM_SUBMIT_DIR

module purge
module load CUDA
python min.py