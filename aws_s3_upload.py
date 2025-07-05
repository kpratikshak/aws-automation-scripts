import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

ACCESS_KEY = ""
SECRET_KEY = ""
LOCAL_FILE = "local_file_name"
BUCKET_NAME = "your_bucket_name"
S3_FILE_NAME = "file_name_on_s3"

def upload_to_s3(local_file, bucket, s3_file):
    s3 = boto3.client(
        's3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful: {s3_file} to {bucket}")
    print("Upload not available")
    return False

result = upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)