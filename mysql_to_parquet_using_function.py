import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pymysql
from azure.storage.blob import BlobServiceClient, ContentSettings

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

########################################
def export_parquet_to_local():
    try:
        with pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_password, db=mysql_db, charset='utf8mb4') as connection:
            # Execute the SQL query and retrieve data as a DataFrame
            data_df = pd.read_sql_query(sql_query, connection)

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
    except Exception as e:
        print(f"An error occurred during the export: {str(e)}")

def upload_parquet_to_azure(account_name, account_key, container_name, blob_name, parquet_file_path, counter):
    try:
        # Upload the Parquet file to Azure Blob Storage with retry logic
        blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
        container_client = blob_service_client.get_container_client(container_name)
        with open(parquet_file_path, "rb") as data:
            max_block_size = 4 * 1024 * 1024
            container_client.upload_blob(
                name=blob_name,
                data=data,
                max_block_size=max_block_size,
                blob_type="BlockBlob",
                content_settings=ContentSettings(content_type="application/parquet")
            )

        print("Parquet file has been uploaded to Azure Blob Storage.")
    except Exception as e:
        print(f"Not able to upload file (attempt {counter}): {str(e)}")
        if counter < 4:
            upload_parquet_to_azure(account_name, account_key, container_name, blob_name, parquet_file_path, counter + 1)
        else:
            print(f"Not able to upload file after {counter} attempts.")

def main():
    # Call the function to export to local
    export_parquet_to_local()
    print("Parquet file has been exported to local")

    # Call the function to upload the Parquet file to Azure with retry logic
    upload_parquet_to_azure(account_name, account_key, container_name, blob_name, parquet_file_path, 1)

if __name__ == "__main__":
    main()
