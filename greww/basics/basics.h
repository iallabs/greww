#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>


#ifndef BASICS_H
#define BASICS_H

// To make sure you don't declare the function more than once by including the header
// multiple times.


using namespace std;

string ConvertToUpper(string str);

const char * string_to_achar(string str);

string achar_to_string(char * achar);
