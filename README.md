# FFT Benchmarking

This script runs a simple suite of FFT benchmarks by varying:
1. the routine used
2. the nearest higher and nearest lower FFT-friendly dimensions of the array

Use as follows:

``
python ftb.py Ny Nx num_tests
``

where

1. Ny is the dimension of the 2D array along the y-axis (index 0)
2. Nx is the dimension of the 2D array along the x-axis (index 1)
3. num_tests is the number of times to run each FFT routine

## Routines tested

1. numpy.fft
2. scipy.fftpack
3. pyfftw + numpy
4. pyfftw + scipy
5. pyfftw + numpy (threaded)
6. pyfftw + scipy (threaded)
7. enlib.fft (pyfftw based)


## Dependencies

1. numpy
2. scipy
3. pyfftw
4. multiprocessing
5. enlib

Enlib is currently a hard dependency. But you only need enlib.fft and enlib.utils,
so if you have just those modules, you can adapt the import command suitably.

(I would recommend just git cloning enlib and adding it to your python path.
The fft and utils modules there don't require any special installation procedures.)