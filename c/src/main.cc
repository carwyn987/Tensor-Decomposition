#include <iostream>
#include <gsl/gsl_sf_bessel.h>
#include <helper.h>

using namespace std;

int main(int argc, char* argv[]){
    cout << "Hello world, pi = " << get_pi() << endl;

    double x = 15.0;
    double y = gsl_sf_bessel_J0 (x);
    printf ("J0(%g) = %.18e\n", x, y);
    
    return 0;
}