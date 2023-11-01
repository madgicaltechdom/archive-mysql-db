from azure.storage.blob import BlobServiceClient
import pyarrow.parquet as pq


# Define your Azure Blob Storage connection string and container name
connect_str = "DefaultEndpointsProtocol=https;AccountName=keshavtesting;AccountKey=H8woyne3OP34rUKEZ1DIfsZwMql+TSA+3ZIjGZcl9P5QVdhyfqvMpaG4DT0evI7rAtNH6ryA6AWD+AStHyJTpQ==;EndpointSuffix=core.windows.net"
container_name = "keshav-sql"
blob_name = "azdata.parquet"

# Initialize a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Get a specific blob from the container
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob data to a local file
downloaded_blob = blob_client.download_blob()
with open("temp.parquet", "wb") as my_blob:
    my_blob.write(downloaded_blob.readall())

# Read the Parquet file
table = pq.read_table('temp.parquet')
df = table.to_pandas()

# Display the DataFrame
print(df)

# Clean up the temporary file
import os
os.remove("temp.parquet")