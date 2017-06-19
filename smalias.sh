# logs

iallog () {
    # return IAL db logs
    # parameters : instance name or id
    python3 /lib/mysql_logs -l $1
}

ialarc () {
    # return instance db architecture
    # parameters : instance name or id
    python3 /lib/mysql_logs -a $1
}

ialarcb () {
    # return ial dabases architecture
    # no parameters
    python /lib/mysql_logs -d
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
    feedjson $1 logs /home/ubuntu/config/ialinst.json
}

feedialarc () {
    # feed ialdbhierarchy.json file
    # parameters values (tuple)
    feedjson $1 arc /home/ubuntu/config/ialdbhierarchy.json
}
