# FFT Benchmarking

Use as follows:

``
python ftb.py Ny Nx num_tests
``

where

1. Ny is the dimension of the 2D array along the y-axis (index 0)
2. Nx is the dimension of the 2D array along the x-axis (index 1)
3. num_tests is the number of times to run each FFT routine

## Dependencies

1. numpy
2. scipy
3. pyfftw
4. multiprocessing
5. enlib

Enlib is currently a hard dependency. But you only need enlib.fft, so if you
have just that module, you can adapt the import command suitably.