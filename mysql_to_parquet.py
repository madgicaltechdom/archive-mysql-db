import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pymysql
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings

# MySQL connection parameters
mysql_host = '127.0.0.1'
mysql_user = 'test'
mysql_password = 'Calmhouse#50'
mysql_db = 'keshav'

# SQL query to retrieve data
sql_query = 'SELECT id,priority,query_description,model_name,updated_at FROM keshav.queue_task_manager limit 1000'

# Specify the Parquet file path
parquet_file_path = 'data.parquet'

# Azure Storage account information
account_name = 'keshavtesting'
account_key = 'H8woyne3OP34rUKEZ1DIfsZwMql+TSA+3ZIjGZcl9P5QVdhyfqvMpaG4DT0evI7rAtNH6ryA6AWD+AStHyJTpQ=='
container_name = 'keshav-sql'
blob_name = 'azdata.parquet'

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
        container_client.upload_blob(name=blob_name, data=data, blob_type="BlockBlob", content_settings=ContentSettings(content_type="application/parquet"))

    print("Parquet file has been uploaded to Azure Blob Storage.")
