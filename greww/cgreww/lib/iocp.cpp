#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#include <iocp.h>

// i o c p
// in/out put c/python

using namespace std;

// Conversion

string ConvertToUpper(string str){
    //Loop through the size of the string
    for(int i=0;i< str.length();i++) {
        //If the character is not a space
        if(str[i] != ' '){
            str[i] = toupper(str[i]);
        }
    }
return str;
}

// string to array of char
//XXX: For the moment python ctypes library doesnt support string types
// every function (if returning a string ) in cpp should be convert it result to char * type

/*
There are, however, enough ways to crash Python with ctypes, so you should be careful anyway.

None, integers, longs, byte strings and unicode strings are the only native Python objects
that can directly be used as parameters in these function calls. None is passed as a C
NULL pointer, byte strings and unicode strings are passed as pointer to the memory block
that contains their data (char * or wchar_t *). Python integers and Python longs are
passed as the platforms default C int type, their value is masked to fit into the C type.

Before we move on calling functions with other parameter types, we have to learn more about
 ctypes data types.
*/


// see https://docs.python.org/2/library/ctypes.html#fundamental-data-types

const char * string_to_achar(string str){
    char res[str.size() + 1];
    strcpy(res, str.c_str());
    return res;
}

// array of char to string

string achar_to_string(char * achar){
    string k(achar);
    return k;
}


// Grew C++/Python Api modeliser



// write files


// write jsons
