import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rezo"
)

parition_names = [ "m202301", "m202302", "m202303", "m202304", "m202305", "m202306", "m202307"]
for parition in parition_names:
    query = "SELECT * FROM rezo.cache PARTITION ({});".format(parition)
    df = pd.read_sql(query, connection)
    # Create a PyArrow table from the data
    table = pa.Table.from_pandas(df)

    # Define a partition-specific Parquet file name
    parquet_file = './export/{}.parquet'.format(parition)

    # Write the data to Parquet
    pq.write_table(table, parquet_file)

