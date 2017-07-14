#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#include "export.h"
//#include "iocp.h"


using namespace std;

extern "C" {
    char * PyWrapper(char * function);
        //string a = string(func);
        //char * b;
        //strcpy(b, string_to_achar(a));
        //return b;
        //cout << "rien";


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

char * PyWrapper(char * function){
    //char * array = new char * [10];
    //array[0] = function;
    //array[1] = target;
    char * res;
    if (strcmp(function, "Export") == 0){
        strcpy(res, "ed");
        return res;
    }
    else {
        strcpy(res, "ka");
        return res;
    }
}

void Export(){

}
