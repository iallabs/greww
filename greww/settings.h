#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>


#ifndef SETTINGS_H
#define SETTINGS_H

// To make sure you don't declare the function more than once by including the header
// multiple times.


using namespace std;

// activate settings

bool make_settings(true);

// os settings

#define working_direction[] = "/home/ubuntu";
#define output_direction[] = "";
#define intput_direction[] = "";

// mysql settings

#define host[] = "";
#define port[] = "";
#define user[] = "";
#define password[] = "";
#define output_mysql[] = "";
#define input_mysql[] = "";

// json settings

#define test_file_json[] = "";
#define output_file_json[] = "";
#define intput_file_json[] = "";

// service settings

// aws

#define aws_key[] = "";
#define aws_secret[] = "";

// servers
#define server_name[] = "";
#define greww_service_working_directory[] = "";
#define server_pem_location[] = "";
#define server_pem_key[] = "";
#define server_ip[] = "";
#define server_hosts[] = "";
#define server_dns[] = "";
#define server_type[] = "";
#define server_home[] = "";
#define server_output[] = "";
#define server_input[] = "";

// backup

#define default_backup_type[] = "";
#define default_backup_directory = "";

// restcom

#define default_com[] = "";
#define com_output[] = "";
#define com_intput[] = "";
