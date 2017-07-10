#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// activate settings

bool make_settings(true);

// os settings

const char working_direction[] = "/home/ubuntu";
const char output_direction[] = "";
const char intput_direction[] = "";

// mysql settings

const char host[] = "";
const char port[] = "";
const char user[] = "";
const char password[] = "";
const char output_mysql[] = "";
const char input_mysql[] = "";

// json settings

const char test_file_json[] = "";
const char output_file_json[] = "";
const char intput_file_json[] = "";

// service settings

// aws

const char aws_key[] = "";
const char aws_secret[] = "";

// servers
const char server_name[] = "";
const char greww_service_working_directory[] = "";
const char server_pem_location[] = "";
const char server_pem_key[] = "";
const char server_ip[] = "";
const char server_hosts[] = "";
const char server_dns[] = "";
const char server_type[] = "";
const char server_home[] = "";
const char server_output[] = "";
const char server_input[] = "";

// backup

const char default_backup_type[] = "";
const char default_backup_directory = "";

// restcom

const char default_com[] = "";
const char com_output[] = "";
const char com_intput[] = "";


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
