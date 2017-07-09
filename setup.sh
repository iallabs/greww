#!/bin/bash

preconfig () {
    pip install -r requirements.txt
}

setup () {
    sudo python3 setup.py install
}

echo "start preconfiguration ..."
preconfig
echo "start setup ..."
setup

exit 0
