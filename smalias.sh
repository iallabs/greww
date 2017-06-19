iallog () {
    python3 /lib/mysql_logs -l $1
}

ialarc () {
    python3 /lib/mysql_logs -a $1
}

ialarcb () {
    python /lib/mysql_logs -d $1
}

newjson () {
    python /lib/json_utils -j -n $1
}

feedjson () {
    python /lib/json_utils -a $1 -t $2 -f $3
}

feediallogs () {
    feedjson $1 logs /home/ubuntu/config/ialinst.json
}

feedialarc () {
    feedjson $1 arc /home/ubuntu/config/ialdbhierarchy.json
}
