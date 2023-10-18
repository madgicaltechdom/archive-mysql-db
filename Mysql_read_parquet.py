import pyarrow.parquet as pq

parquet_file_path = 'data.parquet'  # Replace with your actual Parquet file path

try:
    # Read the Parquet file
    table = pq.read_table(parquet_file_path)
    
    # Convert the Table to a Pandas DataFrame
    df = table.to_pandas()
    
    # Display the DataFrame
    print("Contents of the Parquet file:")
    print(df)
except FileNotFoundError:
    print(f"The file '{parquet_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
