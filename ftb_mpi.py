#!/bin/python

import multiprocessing
import flipper.fft as fftfast
import numpy as np
import time
import sys

from mpi4py import MPI

Nyorig = int(sys.argv[1])
Nxorig = int(sys.argv[2])
N = int(sys.argv[3])

# MPI set up
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
numcores = comm.Get_size()


nthread_fft=multiprocessing.cpu_count()
print "Number of threads: ", nthread_fft, " on rank ", rank

Ny = Nyorig
Nx = Nxorig

A = np.random.normal(0.,1.,(Ny,Nx))

for i in range(1,nthread_fft+1)[::-1]:
    B = fftfast.fft(A,axes=[-2,-1],flags=['FFTW_MEASURE'],nthread=i)

    st = time.time()
    for j in range(N):
        B = fftfast.fft(A,axes=[-2,-1],nthread=i)
    elapsed = time.time()-st
    print "Enlib: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds for ", i, " threads." 




