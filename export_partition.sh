#!/bin/bash

# "panic button" when run in a for loop:
# exit

database="Database_name"
export_dir="path/to/dir"

set -e
echo $export_dir
# reset max exec. time on exit
function cleanup {
  local exit_status=$?
  mysql -u "root" -p -e "SET GLOBAL max_execution_time = 120000;"
  exit $exit_status
}
trap cleanup INT TERM EXIT


start_time=$SECONDS

# switch off query time limit
mysql -u "root" -p -e "SET GLOBAL max_execution_time = 0;"

if [ $# -lt 2 ]; then
  echo "usage export-partition.sh <db_table_name> <time_string>"
  echo "e.g. export-partition.sh yearly_archived_table y2011"
  echo "or   export-partition.sh monthly_archived_table m201911"
  echo "or   export-partition.sh weekly_archived_table w201950"
  exit 1
fi

table=$1
shift
time_string=$1
shift
temp_table="${table}_${time_string}"
export_file_name=$temp_table

# count rows in partition
echo "Counting rows in partition ${table}#${time_string}..."
rows=`mysql -u "root" -p $database -Nse "SELECT COUNT(*) FROM $table PARTITION($time_string)"`
echo "Found $rows row in partition"

echo "Exchanging ${table}#${time_string} partition to ${temp_table}"
mysql -u "root" -p $database -e "CREATE TABLE $temp_table LIKE $table"
mysql -u "root" -p $database -e "ALTER TABLE $temp_table REMOVE PARTITIONING"
mysql -u "root" -p $database -e "ALTER TABLE $table EXCHANGE PARTITION $time_string WITH TABLE $temp_table"

# sanity check
count=`mysql -u "root" -p $database -Nse "SELECT COUNT(*) FROM $temp_table"`
echo "Found $count rows in $temp_table"
if [ $rows = $count ]; then
  echo "Sanity check OK!"
else
  echo "Sanity check failed: $rows rows vs. $count count"
  exit 1
fi

echo "Exporting $temp_table to $export_dir/$table/$export_file_name.gz"
mkdir -p $export_dir/$table
mysqldump -u "root" -p --create-options --single-transaction \
          $database $temp_table | gzip -f > $export_dir/$table/$export_file_name.gz
ls -lh $export_dir/$table/$export_file_name.gz

echo "Dropping table $temp_table"
mysql -u "root" -p $database -e "DROP TABLE $temp_table"

echo "Dropping partition ${table}#${time_string}"
mysql -u "root" -p $database -e "ALTER TABLE $table DROP PARTITION $time_string"

elapsed_time=$(($SECONDS - $start_time))
echo "Done in $(($elapsed_time / 60)) min $(($elapsed_time % 60)) sec"

echo