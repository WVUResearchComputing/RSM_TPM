# Response Surface Model + Test Particle Model (RSM+TPM)

RSM+TPM is a code written in Python and C

RSM is written in Python and TPM is written in C

## Test Particle Model

The Test Particle Model (TPM) is written in C and uses MPI and some extra libraries.

To compile TPM several packages are needed:

  * C compiler
  * GSL libraries
  * HDF5 libraries (Serial version is enough)
  * MPI implementation and libraries
  * Autoconf needed if installing from the Github repository
  * Git to clone the repository

To install these dependencies you can use the packages provided by your Linux distribution
For example on Ubuntu focal the dependencies above can be satisfied executing the command:

```
	sudo apt-get install build-essential git autoconf libgsl-dev libhdf5-dev libmpich-dev
```

## Response Surface Model

The Response Surface Model (RSM) is written in Python and uses this Python packages:

  * Python version 3+ (Tested on Python 3.8+)
  * Numpy
  * Matplotlib
  * Pandas
  * sklearn
  * h5py

You can install these dependencies using the packages on the Linux distribution.
On Ubuntu focal you can install most dependencies executing the command:

```
	sudo apt-get install python3 python3-numpy python3-matplotlib python3-pandas python3-sklearn python3-pip
```

An exception  here is h5py. The package provided by Ubuntu depends on OpenMPI.
To install the serial version use pip:

```
	sudo python3 -m pip install h5py
```

## Cloning the repository

Clone the repository from Github using the git command:

```
git clone https://github.com/WVUResearchComputing/RSM_TPMC.git
```

or

```
git clone https://github.com/ASSISTLaboratory/WVU_RSM_Suite.git
```

## Compile TPM

Go to the folder `TSM_TPMC/tpm` and prepare the sources for compilation:

```
cd TSM_TPMC/tpm
./autogen.sh
```

Execute the script `./configure`. One important option is to enable MPI so the code can work on multiple CPU cores or even distributed across multiple compute nodes.

```
./configure --enable-mpi
```

Other options availble include adding debugging and/or profiling flags. Enabling this features is useful for developers but will create a slower executable

```
./configure --enable-mpi --enable-debug --enable-gprof
```

If everything is correct at this point, the configure will have detected the location for GSL, HDF5 and the proper way of adding MPI support to the code.
Compile the code with:

```
make
```

## Execute RSM

The main script for RSM is `rsm_run_script.py`.
You can execute this script with two options `--mpiexec` and `--tpm`. This options will select which will be the MPI execution command and the location of the tpm executable.
The values for default are equivalent to use this command:

```
./rsm_run_script.py --mpiexec=mpiexec --tpm=tpm/src/tpm
```


