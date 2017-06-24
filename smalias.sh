# logs
iallog () {
    # return IAL db logs
    # parameters : instance name or id from ialinst.json
    python3 /lib/mysql_logs -l $1
}

ialuser () {
    python3 /lib/mysql_logs -u $1
}

ialpd () {
    python3 /lib/mysql_logs -pd $1
}

abstract_mysql_syntax () {
    echo -u $(ialuser $1) -p $(ialpd $1)
}

ialarc () {
    # return instance base db architecture
    # parameters : instance name or id from ialhierarchy.json
    python3 /lib/mysql_logs -a $1
}

# jsons



newjson () {
    # create json file
    # parameters : file name or path
    python /lib/json_utils -j -n $1
}

feedjson () {
    # add values to json file
    # parameters : values (tuple),
    #              type ('logs' or 'arc')
    #              filepath ('/*')
    python /lib/json_utils -a $1 -t $2 -f $3
}

feediallogs () {
    # feed ialinst.json file
    # parameters values (tuple)
    feedjson $1 logs /home/ubuntu/data/instances.json
}

feedialarc () {
    # feed ialdbhierarchy.json file
    # parameters values (tuple)
    feedjson $1 arc /home/ubuntu/data/hierarchy.json
}

# mysql_manage

info_msql_instance () {
    python3 /lib/mysql_manage.py -i $1
}

this_instance () {
    echo file.txt lien 1
}

prepare_backend_storage_db () {
    mkdir /home/ubunt/output/backend_temp.sql
    mysqldump abstract_mysql_syntax $(this_instance) $1 > /home/ubunt/output/backend_temp.sql
}

prepare_backend_storage () {

}
