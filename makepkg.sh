#!/bin/bash

mysql_info () {
    kr="/home/ubuntu/IAL/mysql_utils/ialsql/manage.py"
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
    python3 /home/ubuntu/IAL/mysql_utils/ialsql/manage.py -i
}

mysql_access () {
    python3 $1
}

mysql_data () {
    python3 $1
}

jmysql_manage () {
    python3 $1
}

mysql_cmdline () {

}


$@
