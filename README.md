# Rezo-MySQL
If you're looking to manage MySQL connections and run SQL queries directly within Visual Studio Code, you can use an extension like "MySQL" or "SQL Server (mssql)".For instance, the "MySQL" extension allows you to set up connections and execute SQL queries. 

## Step of performing operation:

 1.Install the Extension:

- Open Visual Studio Code.
- Click on the "Extensions" icon in the sidebar (four squares icon on the left side).
- Search for "MySQL" and install the "MySQL" extension provided by Jun Han.
  
 2. Configure a Connection:

- Open your .sql file that contains the SQL code to create the cache table.
- Above the SQL code, you should see a green "Run Query" button.
- To the right of this button, you should see a "MySQL" logo. Click on it.
- A "MySQL" tab will appear below. In the "MySQL Connections" tab, click on the gear icon to configure a new connection.
## Add Connection Details:

- Click on "Add Connection."
- Fill in the connection details for your MySQL server, such as server address, port, username, password, and database.
- After entering the details, click "Connect" to establish the connection.
  
## Run the Query:

- Now that your connection is configured, go back to your .sql file with the SQL code.
- Click on the green "Run Query" button to execute the SQL code on the connected MySQL database.


Always exercise caution when running SQL queries on databases, especially if you're working with production data. It's advisable to test queries on a development or testing environment before applying them to production databases.
