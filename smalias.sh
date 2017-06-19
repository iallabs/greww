iallog () {
    python3 /lib/mysql_logs -l $1
}

ialarc () {
    python3 /lib/mysql_logs -a $1
}

ialarcb () {
    python /lib/mysql_logs -d $1
}
