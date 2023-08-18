#!/bin/bash

function usage {
  echo "Use ./run_ghost.sh table_name 'alter_command' [other_ghost_args]"
  exit 1
}

database="mad"
password="9431"
host="localhost"
user="root"
MYSQL_CMD="mysql"
# Execute the SQL commands from alter_tables.sql
$MYSQL_CMD -u $user -p$password $database < alter_tables.sql
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
         --initially-drop-ghost-table --initially-drop-socket-file  --initially-drop-old-table\
         --verbose $*