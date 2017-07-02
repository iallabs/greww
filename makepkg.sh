#!/bin/bash


output="/home/ubunutu/data"

alias mysql='/bin/'

mysql_info () {
    kr="/home/ubuntu/IAL/mysql_utils/ialsql/manage.py"
    # vm=$1
    # db=$2
    # tb=$3
    # sl=$4
    if [ -z $1 ]; then
        if [ -z $2 ]; then
            if [ -z $3 ]; then
                if [ -z $4 ]; then
                    python3 $kr -i -vm $1 -db $2 -tb $3 -sl $4
                else
                    python3 $kr -i -vm $1 -db $2 -tb $3
                fi
            else
                python3 $kr -i -vm $1 -db $2
            fi
        else
            python3 $kr -i -vm $1
        fi
    fi
}

mysql_access () {
    kr="/home/ubuntu/IAL/mysql_utils/ialsql/manage.py"
    # vm=$1
    # db=$2
    # tb=$3
    # elem=$4
    # extra=$5
    python3 $kr
}

mysql_backend () {
    if [ $1="build" ]; then
        #
    elif [ $1="generate" ]; then
        #
    fi
}





$@
