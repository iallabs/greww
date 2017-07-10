#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>


#ifndef BASICS_H
#define BASICS_H

// To make sure you don't declare the function more than once by including the header
// multiple times.


using namespace std;

// conversion

string ConvertToUpper(string str);

const char * string_to_achar(string str);

string achar_to_string(char * achar);


// CppPython modeliser

const char * code_string_array(string * astr);

const char * code_int_array(string * astr);

string * decode_string_array(string str);

int * decode_int_array(string str);

// write result in files



// write result as json
