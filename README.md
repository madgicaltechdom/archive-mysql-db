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
- On the left bottom you can see "MYSQL" below "OUTLINE" and "TIMELINE" near the Setting icon.
   On hover, you can see "+". Click on it.
- Then provide details like "host", "user", "password", "port" etc.
-   And then press enter. Your connection will be added.

3. Run the following command to ALTER TABLE Command:

 ```
   ALTER TABLE cache DROP INDEX search_query;
 ```
4. Run the command  to ALTER TABLE Command:

```
ALTER TABLE cache DROP INDEX id_UNIQUE;

ALTER TABLE cache MODIFY created_at Datetime;
```

5. Run Query:
- Open your .sql file that contains the SQL code and provide the database name to create the cache/insert table.
- Right-click on the file then click on the "Run Query" button.
- Your query will run and successful message you can see in the terminal.
6. Run the command to show the table
  
```
SHOW CREATE TABLE cachet;
```

Always exercise caution when running SQL queries on databases, especially if you're working with production data. It's advisable to test queries on a development or testing environment before applying them to production databases.

## My Sql large tables Archiving
### Steps for Archiving [video](https://drive.google.com/file/d/13XYQ_gdBlxuHMapFnvCGQxcrUg-js9e7/view)
1. Clone repo:
````
 https://github.com/madgicaltechdom/rezo-mysql/tree/mysql-archieve-latest
````
2. Install gh-ost [tool]( https://github.com/github/gh-ost/releases/tag/v1.1.5)
3. Keep the tool and repo in the same folder or give the path to gh-ost tool in all script files where "./gh-ost" is called.
4. Preparing tables for partitioning
- Open run_ghost.sh file . Fill in credentials (Database name, host, Password, etc)
- Then Run
```
 ./run_ghost.sh cachet "PARTITION BY RANGE (TO_DAYS(created_at)) (
    PARTITION m202301 VALUES LESS THAN (TO_DAYS('2023-02-01')),
    PARTITION m202302 VALUES LESS THAN (TO_DAYS('2023-03-01')),
    PARTITION m202303 VALUES LESS THAN (TO_DAYS('2023-04-01')),
    PARTITION m202304 VALUES LESS THAN (TO_DAYS('2023-05-01')),
    PARTITION m202305 VALUES LESS THAN (TO_DAYS('2023-06-01')),
    PARTITION m202306 VALUES LESS THAN (TO_DAYS('2023-07-01')),
    PARTITION m202307 VALUES LESS THAN (TO_DAYS('2023-08-01')),
    PARTITION m202308 VALUES LESS THAN (TO_DAYS('2023-09-01')),
    PARTITION future VALUES LESS THAN (MAXVALUE)
)"

```
 in the terminal and go to the directory where the file is located.
- Finally, Partition will be created. You can change the above query according to your requirement like a partition on the basis of month or column name or increase/decrease no of partition etc.
5. Exporting old data from the table
- Open export_partition.sh file, Provide credentials like database name and export_dir
- Run
```
  ./export_partition.sh table_name partition_name
```
  in the terminal and go to the directory where the file is located.
- Provide MySQL password again and again if asked
- Finally, your file will be created in the directory you provided in the script file if all the steps run successfully.
6. Restoring data from the archive
- Run
  ```
   gunzip /export_dir/filename.gz | MySQL -u root -p
  ```
  in the terminal and go to the directory where the file is located.
- Your file will be restored.
### Steps for Automation
1. The above partition Query contains some pattern so that the automation script reads the value on the basis of the partition name so create a partition by using the above query or create a query like the above in the same pattern according to your requirement.
2. Before running the automated script Make sure the table is already partitioned
3. In the .txt file fill the details ( like cache monthly 2  from line 9 that is table_name, interval, partition you want to keep)
4. Provide credentials like database name etc
5. Run bash ./autoarchive-tables.sh in the terminal and go to the directory where the file is located.
6. Provide MySQL password again and again if asked
7. Finally if all your commands run successfully then you can see the dump file is created in the cache(table name) folder.
## Output:
![Screenshot 2023-08-14 at 3 06 46 PM](https://github.com/madgicaltechdom/rezo-mysql/assets/109335469/87f44afd-91df-4d5b-a75f-0546db269c20)
![Screenshot 2023-08-14 at 3 07 00 PM](https://github.com/madgicaltechdom/rezo-mysql/assets/109335469/ed0f9c44-e03f-4417-b67a-ba44bbde471e)
![Screenshot 2023-08-14 at 3 07 15 PM](https://github.com/madgicaltechdom/rezo-mysql/assets/109335469/f4a1696b-2fae-4d95-afc0-e6a3a16a874f)
   
## Additional Resources
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [MySQL Workbench Documentation](https://dev.mysql.com/doc/workbench/en/)

  ## References
  we have taken help from this [article](https://dev.to/nejremeslnici/archiving-large-mysql-tables-part-i-intro-4im1) 
  
