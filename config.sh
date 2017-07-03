#!/bin/bash

preconfig () {
    mkdir /home/ubuntu/data/mysqlbackends
    sudo apt install mysql-server
    echo "created /home/ubuntu/data/mysqlbackends"
}


config () {
    echo "mysql server configurations"
    sudo service mysql start
}

preconfig && config

exit 0
