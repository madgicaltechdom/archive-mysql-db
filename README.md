## Rezo-MySQL
If you're looking to manage MySQL connections and run SQL queries directly within Visual Studio Code, you can use an extension like "MySQL" or "SQL Server (mssql)".For instance, the "MySQL" extension allows you to set up connections and execute SQL queries. 
This document provides instructions for setting up and managing a MySQL database connection for your application. Follow the steps below to establish a connection to your MySQL database.

## Prerequisites
- MySQL Server is installed and running.
- Credentials (username and password) with appropriate privileges to access the desired database.

## Connection Parameters
- Host: The hostname or IP address of the MySQL server.
- Port: The port number on which the MySQL server is running (default: 3306).
- Database: The name of the target database.
- Username: The username with access to the database.
- Password: The password associated with the username.

  ## Add Connection Details:

- Click on "Add Connection."
- Fill in the connection details for your MySQL server, such as server address, port, username, password, and database.
- After entering the details, click "Connect" to establish the connection.
## Installation Steps:
To configure your system using this repository, follow these steps:


1. Clone the repository to your local machine by running the below command:

```
git clone https://github.com/madgicaltechdom/rezo-mysql
```
## Step of performing operation: [video](https://drive.google.com/file/d/18FqgshsfDs1wlN9qG178P9bOByEkb6ii/view)

 1. Install the Extension:

- Open Visual Studio Code.
- Click on the "Extensions" icon in the sidebar (four squares icon on the left side).
- Search for "MySQL" and install the "MySQL" extension provided by Jun Han.
  
 2. Configure a Connection:

- Open your .sql file that contains the SQL code to create the cache table.
- Above the SQL code, you should see a green "MySQL" button in the left corner bottom.
- To the right of this button, you should see a "+" logo. Click on it.
- A "MySQL" tab will appear below. In the "MySQL Connections" tab, click on the "+" for new connection.

 3. Run the Query:

- Now that your connection is configured, go back to your .sql file with the SQL code.
- Click on the green "Run Query" button to execute the SQL code on the connected MySQL database.

                                     or
- Open your .sql file that contains the SQL code and provide the database name to create the cache/insert table.
- Right-click on the file then click on the "Run Query" button.
- Your query will run and successful message you can see in the terminal.

Always exercise caution when running SQL queries on databases, especially if you're working with production data. It's advisable to test queries on a development or testing environment before applying them to production databases.

## My Sql large tables Archiving
### Steps for Archiving 
1. Clone repo:
````
 https://github.com/madgicaltechdom/rezo-mysql/tree/mysql-archieve-latest
````
4. Install gh-ost [tool] ( https://github.com/github/gh-ost/releases/tag/v1.1.5)
5. Keep the tool and repo in the same folder or give the path to gh-ost tool in all script files where "./gh-ost" is called.
6. Preparing tables for partitioning
- Open run_ghost.sh. Fill credentials (Database name, host, Password, etc)
- Then Run "PARTITION BY RANGE(TO_DAYS(created_at)) (PARTITION p0 VALUES LESS THAN (TO_DAYS('2023-01-01')), PARTITION p1 VALUES LESS THAN (TO_DAYS('2023-02-01')), PARTITION p2 VALUES LESS THAN (TO_DAYS('2023-03-01')), PARTITION p3 VALUES LESS THAN (TO_DAYS('2023-04-01')), PARTITION p4 VALUES LESS THAN (MAXVALUE))" --execute" in the terminal and go to directory where file is located.
- Finally, Partition will be created. You can change the above query according to your requirement like a partition on the basis of month or column name or increase/decrease no of partition etc.
5. Exporting old data from the table
- Open export_partition.sh. Provide credentials like database name and export_dir
- Run ./export-partition.sh table_name partition_name in the terminal and go to the directory where the file is located.
- Provide mysql password again and again if asked
- Finally, your file will be created in the directory you provided in the script file if all the steps run successfully.
6. Restoring data from the archive
- Run gunzip /export_dir/filename.gz | MySQL -u root -p in the terminal and go to the directory where the file is located.
- Your file will be restored.
### Steps for Automation
1. After creating the table, create a partition by "PARTITION BY RANGE (TO_DAYS(created_at)) (
PARTITION m202301 VALUES LESS THAN (TO_DAYS('2023-02-01')),
PARTITION m202302 VALUES LESS THAN (TO_DAYS('2023-03-01')),
PARTITION m202303 VALUES LESS THAN (TO_DAYS('2023-04-01')),
PARTITION m202304 VALUES LESS THAN (TO_DAYS('2023-05-01')),
PARTITION m202305 VALUES LESS THAN (TO_DAYS('2023-06-01')),
PARTITION m202306 VALUES LESS THAN (TO_DAYS('2023-07-01')),
PARTITION m202307 VALUES LESS THAN (TO_DAYS('2023-08-01')),
PARTITION m202308 VALUES LESS THAN (TO_DAYS('2023-09-01')),
PARTITION future VALUES LESS THAN (MAXVALUE)")
2. The above partition Query contains some pattern so that the automation script reads the value on the basis of the partition name so create a partition by using the above query or create a query like the above in the same pattern according to your requirement.
3. Before running the automated script Make sure the table is already partitioned
4. In the .txt file fill the details ( like cache monthly 2  from line 9 that is table_name, interval, partition you want to keep)
5. Provide credentials like database name etc
6. Run bash ./autoarchive-tables.sh in the terminal and go to the directory where the file is located.
7. Provide MySQL password again and again if asked
8. Finally if all your commands run successfully then you can see the dump file is created in the cache(table name) folder.
## Additional Resources
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [MySQL Workbench Documentation](https://dev.mysql.com/doc/workbench/en/)
