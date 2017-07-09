#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// activate settings

bool mksettings(true);

// os settings

const char working_direction[] = "/home/ubuntu";
const char output_direction[] = "/home/ubuntu/op";
const char intput_direction[] = "/home/ubuntu/ip";

// mysql settings

const char working_direction[] = "/home/ubuntu";
const char output_direction[] = "/home/ubuntu/op";
const char intput_direction[] = "/home/ubuntu/ip";

// json settings

const char working_direction[] = "/home/ubuntu";
const char output_direction[] = "/home/ubuntu/op";
const char intput_direction[] = "/home/ubuntu/ip";

// service settings

const char working_direction[] = "/home/ubuntu";
const char output_direction[] = "/home/ubuntu/op";
const char intput_direction[] = "/home/ubuntu/ip";


extern "C" {
    const char * vrcaller(const char * a)
    {
        if (strcmp(a,"wdir") == 0){
            return working_direction;
        }
        if (strcmp(a,"odir") == 0){
            return output_direction;
        }
        if (strcmp(a, "idir") == 0){
            return input_direction;
        }

        return "NaN";
    }
}


/* direction

*
*

*
*

*
*

*
*


*
*


*
*



*/
