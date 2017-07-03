#!/bin/bash

preconfig () {
    pip3 install pymysql
}

setup () {
    sudo python3 setup.py install
}

echo "start preconfiguration ..."
preconfig
echo "start setup ..."
setup

exit 0
