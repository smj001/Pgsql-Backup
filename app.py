import os
import psycopg2
import subprocess
import boto3
import jdatetime


# PostgreSQL database credentials
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

# S3 credentials
s3_access_key = os.environ.get('S3_ACCESS_KEY')
s3_secret_key = os.environ.get('S3_SECRET_KEY')
s3_bucket_name = os.environ.get('S3_BUCKET_NAME')

# S3 endpoint

s3_endpoint_url = os.environ.get('S3_HOST')

# File Date
day = jdatetime.datetime.now().day
month = jdatetime.datetime.now().month
year = jdatetime.datetime.now().year
hour = jdatetime.datetime.now().hour
file_date = f"{year}-{month}-{day}-{hour}"

# Connect to the PostgreSQL database and retrieve a list of database names
conn = psycopg2.connect(host=db_host, port=db_port, user=db_user, password=db_password)
cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
rows = cur.fetchall()

# Loop through the database names and create backups
for row in rows:
    db_name = row[0]
    backup_file = db_name + f"{file_date}.backup"
    backup_path = os.path.join(os.getcwd(), backup_file)
    backup_command = f"pg_dump -Fc -h {db_host} -p {db_port} -U {db_user} -d {db_name} -f {backup_path}"
    subprocess.run(backup_command, shell=True)

    # Upload the backup file to S3
    s3 = boto3.client(
        "s3",
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
        endpoint_url=s3_endpoint_url,
    )
    s3.upload_file(backup_path, s3_bucket_name, backup_file)

# Close the database connection
cur.close()
conn.close()
