# mysql_utils
IAL python kit for mysql and json operations


# installation

```shell
git clone https://github.com/ImperialAlphaLab/mysql_utils
bash makepkg.sh
source mysql_utils.sh
```

# Use examples
### General description

```shell
USER$ source mysql_utils.sh
USER$ mysql_utils -h
> Top level options
 -i --information
 -sio --sysio
 -a --add
 -f --find
> Options
 -vm --virtualmachine
 -db --database
 -tb --table
 -sl --selection
```

###### IAL-Central databases

```shell
USER$ mysql_utils -i -vm IAL-Central //-X to expand
#-- VM :  IAL-Central
#------------------ DATABASES
#------------------ information_schema
#------------------ AMINE
#------------------ test1
#------------------ performance_schema
#------------------ sys
```

###### IAL-Central test1 databases tables

```shell
USER$ mysql_utils -i -vm IAL-Central -db test1
#-- VM :  IAL-Central
#------------- :  test1
#---------------------------- : TABLES
#---------------------------- : columns_priv
#---------------------------- : db
#---------------------------- : engine_cost
#---------------------------- : event
#---------------------------- : func
#---------------------------- : general_log
#---------------------------- : gtid_executed
#---------------------------- : help_category
#---------------------------- : help_keyword
#---------------------------- : help_relation
#---------------------------- : help_topic
#---------------------------- : innodb_index_stats
#---------------------------- : innodb_table_stats
#---------------------------- : ndb_binlog_index
#---------------------------- : plugin
#---------------------------- : proc
#---------------------------- : procs_priv
#---------------------------- : proxies_priv
#---------------------------- : server_cost
#---------------------------- : servers
#---------------------------- : slave_master_info
#---------------------------- : slave_relay_log_info
#---------------------------- : slave_worker_info
#---------------------------- : slow_log
#---------------------------- : tables_priv
#---------------------------- : time_zone
#---------------------------- : time_zone_leap_second
#---------------------------- : time_zone_name
#---------------------------- : time_zone_transition
#---------------------------- : time_zone_transition_type
#---------------------------- : user

```

###### Table fields

```shell
USER$ source mysql_utils.sh -i -vm IAL-Central -db test1 -tb servers
 #-- VM :  IAL-Central
 #------------- :  mysql
 #----------------- :  servers
['Server_name', 'Host', 'Db', 'Username', 'Password', 'Port', 'Socket', 'Wrapper', 'Owner']

```
