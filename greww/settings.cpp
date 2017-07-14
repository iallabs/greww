/*
    settings constants api
*/
#include <settings.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


extern "C" {
    const char * GeneralSettings(const char * a)
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
        if (strcmp(a,"mysql_settings") == 0){
            // return working_direction;
            //TODO: need return all settings ? maybe
        }
        if (strcmp(a,"json_settings") == 0){
            //TODO: same
        }
        if (strcmp(a,"aws_settings") == 0){
            //TODO: same
        }
        if (strcmp(a,"backup_settings") == 0){
            //TODO: same
        }
        if (strcmp(a,"service_settings") == 0){
            //TODO: same
        }
        if (strcmp(a,"server_settings") == 0){
            //TODO: same
        }
        if (strcmp(a,"restcom_settings") == 0){
            //TODO: same
        }

        return "NaN";
    }
}

//
//
