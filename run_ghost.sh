#!/bin/bash

function usage {
  echo "Use ./run_ghost.sh table_name 'alter_command' [other_ghost_args]"
  exit 1
}
MYSQL_PASSWORD=$(cat mysql_password.txt)

database="DatabaseName"
host="HostName"
user="UserName"
password=$MYSQL_PASSWORD

table=$1
shift

if [ "$table" == "" ]; then
  usage
fi

alter=$1
shift

if [ "$alter" == "" ]; then
  usage
fi

cut_over_file=/root/bin/gh-ost-cut-over.txt
touch $cut_over_file

./gh-ost --host=$host \
         --database=$database \
         --user=$user \
         --password=$password \
         --table=$table \
         --alter="$alter" \
         --chunk-size=2000 --max-load=Threads_connected=50 \
         --allow-on-master --ssl --ssl-allow-insecure --exact-rowcount \
         --allow-nullable-unique-key \
         --initially-drop-ghost-table --initially-drop-socket-file  --initially-drop-old-table\
         --verbose $*