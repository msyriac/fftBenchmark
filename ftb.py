#!/bin/python

from numpy.fft import fft2 as nfft2
from scipy.fftpack import fft2 as sfft2

from pyfftw.interfaces.scipy_fftpack import fft2 as psfft2
from pyfftw.interfaces.numpy_fft import fft2 as pnfft2

import numpy as np
import time
import multiprocessing
from enlib import fft as fftfast

import sys


Nyorig = int(sys.argv[1])
Nxorig = int(sys.argv[2])
N = int(sys.argv[3])

Nxdown = fftfast.fft_len(Nxorig,direction="below")
Nydown =  fftfast.fft_len(Nyorig,direction="below")
Nxup = fftfast.fft_len(Nxorig,direction="above")
Nyup =  fftfast.fft_len(Nyorig,direction="above")

nthread_fft=multiprocessing.cpu_count()
print "Number of threads: ", nthread_fft

print "Starting benchmarks..."

i=0
for Ny,Nx,label in [(Nyorig,Nxorig,"original"),(Nydown,Nxdown,"smaller"),(Nyup,Nxup,"larger")]:

    print "==============================="
    print label, " length (",Ny,",",Nx,")"
    print "==============================="
    if i>0 and Ny==Nyorig and Nx==Nxorig:
        print "Already done. Skipping."
        continue
    
    A = np.random.normal(0.,1.,(Ny,Nx))



    # st = time.time()
    # for j in range(N):
    #     B = nfft2(A)
    # elapsed = time.time()-st
    # print "Numpy: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds."

    # st = time.time()
    # for j in range(N):
    #     B = sfft2(A)
    # elapsed = time.time()-st
    # print "Scipy: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds."

    # B = pnfft2(A)
    # st = time.time()
    # for j in range(N):
    #     B = pnfft2(A)
    # elapsed = time.time()-st
    # print "pyfftw-numpy: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds."


    # st = time.time()
    # for j in range(N):
    #     B = psfft2(A)
    # elapsed = time.time()-st
    # print "pyfftw-scipy: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds."


    st = time.time()
    for j in range(N):
        B = pnfft2(A,threads=nthread_fft)
    elapsed = time.time()-st
    print "Threaded pyfftw-numpy: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds."


    st = time.time()
    for j in range(N):
        B = psfft2(A,threads=nthread_fft)
    elapsed = time.time()-st
    print "Threaded pyfftw-scipy: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds."


    B = fftfast.fft(A,axes=[-2,-1],flags=['FFTW_MEASURE'])
    st = time.time()
    for j in range(N):
        B = fftfast.fft(A,axes=[-2,-1])
    elapsed = time.time()-st
    print "Enlib: ", '{:.2f}'.format(elapsed*1000./N), " milliseconds."

    i+=1
