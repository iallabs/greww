#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#include "export.h"
//#include "iocp.h"


using namespace std;

extern "C" {
    void wrap_function(){
        //string a = string(func);
        //char * b;
        //strcpy(b, string_to_achar(a));
        //return b;
        cout << "rien";
    }

    /*
    char* get_function_module(string function){
       return "NotImplemented";
    }

    char* get_object_module(string object){
       return "NotImplemented";
    }

    char* get_value_module(string value){
       return "NotImplemented";
    }
    */
}
