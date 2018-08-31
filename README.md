# mysql-tools

Script storage space used for mysql operation

## Required

It is necessary to add environment variable

example

```
export MONITORING_DB_USER='DB UserName'
export MONITORING_DB_PASS='DB Passowrd'
```

## Execution

### check-replication-status

Check the replication status of mysql

- Slave_IO_Running
- Slave_SQL_Running
- Seconds_Behind_Master

```
# It will be executed as many times as specified in the argument

$ python ./mysql-tools/check-replication-status.py [DBHost or IPAddress] ...

result example:
"Target DBHost or IPAddress"
Slave_IO_Running: Yes, Slave_SQL_Running: Yes, Seconds_Behind_Master: 0
"Target DBHost or IPAddress"
Slave_IO_Running: Yes, Slave_SQL_Running: Yes, Seconds_Behind_Master: 0


```
