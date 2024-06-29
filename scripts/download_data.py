import os
import boto3
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# load .env 文件
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
REGION = 'your_region'

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)

# Download Parquet file
parquet_file = 'raw_data/raw_data.parquet'
s3.download_file(AWS_S3_BUCKET_NAME, parquet_file, parquet_file)

# Read Parquet file
df = pd.read_parquet(parquet_file)

# Filter data to keep only rows where events contain "206"
df_filtered = df[df['events'].str.contains('206')]

# Connect to MySQL database
engine = create_engine(f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}')
conn = engine.connect()

# Write data to MySQL database
df_filtered.to_sql('filtered_data', conn, if_exists='replace', index=False)

conn.close()