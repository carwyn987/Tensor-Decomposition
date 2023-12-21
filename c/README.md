Compilation steps:

```
$ make
$ export LD_LIBRARY_PATH=/home/carwyn/gsl/lib/
$ ./build/out
```

Depreciated Basic C++ Compilation Instructions

A simple compilation can be performed with:
```
$ g++ -o a.out main.cc helper.cc -I.
```
Where:
 - g++ is the GNU c++ compiler
 - -o main specifies the "target name", i.e. the output executable name
 - -I. adds "." to the compilers search path.



Setup of GNU Scientific Library (GSL)
 - https://coral.ise.lehigh.edu/jild13/2016/07/11/hello/

Depreciated GSL incorporated compilation steps:

```
gcc -Wall -I/home/carwyn/gsl/include -c src/main.cc
gcc -L/home/carwyn/gsl/lib main.o -lgsl -lgslcblas -lm
export LD_LIBRARY_PATH=/home/carwyn/gsl/lib/
./a.out
```
Or succinctly:
```
make
export LD_LIBRARY_PATH=/home/carwyn/gsl/lib/
./build/a.out
```