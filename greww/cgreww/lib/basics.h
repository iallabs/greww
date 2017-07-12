#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

// In Out C Python

#ifndef BASICS_H
#define BASICS_H
#endif

// To make sure you don't declare the function more than once by including the header
// multiple times.


using namespace std;


const char* GetFunctions(string function);

void mkfile(string directory, string name, string ext);

void mkfile_with_content(string directory, string name, string ext, string content);

int file_lenght();
