Basic C++ Compilation Instructions

A simple compilation can be performed with:
$ g++ -o a.out main.cc helper.cc -I.
Where:
 - g++ is the GNU c++ compiler
 - -o main specifies the "target name", i.e. the output executable name
 - -I. adds "." to the compilers search path.

