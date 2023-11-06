import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pymysql
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings

# MySQL connection parameters
mysql_host = 'db.mysql.database.azure.com'
mysql_user = 'db'
mysql_password = 'Z'
mysql_db = 'l'

# Azure Storage account information
account_name = 'testing'
account_key = '=='
container_name = 'sql'
blob_name = 'oc.parquet'

# SQL query to retrieve data
sql_query = 'SELECT * FROM abc'

# Specify the Parquet file path
parquet_file_path = 'oc.parquet'

############################################################################################

# Establish MySQL connection
connection = pymysql.connect(host=mysql_host,user=mysql_user,password=mysql_password,db=mysql_db,charset='utf8mb4')

# Execute the SQL query and retrieve data as a DataFrame
data_df = pd.read_sql_query(sql_query, connection)

# Close MySQL connection
connection.close()

# Check if the DataFrame is empty (contains only column headers)
if data_df.empty:
    print("The DataFrame is empty (contains only column headers). No data to export.")
else:
    # Display the DataFrame to verify the data
    print(data_df.head())

    # Convert the DataFrame to an Arrow Table
    table = pa.Table.from_pandas(data_df)

    # Write the Arrow Table to a Parquet file
    pq.write_table(table, parquet_file_path)

    print('Data has been exported to Parquet file:', parquet_file_path)
    
    # Upload the Parquet file to Azure Blob Storage
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
    container_client = blob_service_client.get_container_client(container_name)
    with open(parquet_file_path, "rb") as data:
        max_block_size = 4*1024*1024
        container_client.upload_blob(name=blob_name, data=data,max_block_size=max_block_size, blob_type="BlockBlob", content_settings=ContentSettings(content_type="application/parquet"))

    print("Parquet file has been uploaded to Azure Blob Storage.")
