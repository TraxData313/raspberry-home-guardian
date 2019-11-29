import os
import time
import boto3
from botocore.exceptions import ClientError
import time
from loggers import log_event, log_error 


# - Function that upoads files to S3:
def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as error_message:
        log_error(reporting_program_name, error_message)
        return False
    return True
    

# - Initialize variables:
files = []
filesExistBool = 0
reporting_program_name = 'file_monitor.py'

# - Recover the bucket name from the settings file:
bucket_name = open('settings.txt', 'r').readlines()
bucket_name = str(bucket_name[1])
bucket_name = bucket_name[:-1]

# - Log starting program event:
event_message = 'Starting program'
log_event(reporting_program_name, event_message)

while True:
    # - Check for files:
    del files
    files = os.listdir("./media")
    for file in files:
        # - Rename the file (add the path to it):
        file =  "media/" + file
        # - Upload the file to the S3 bucket:
        print(" ")
        temp_str = "file_monitor.py: Found file", file, ". Uploading..."
        print(temp_str)
        try:
            upload_file(file_name=file, bucket=bucket_name)
            print("- uploaded!")
            # - Remove the file:
            os.remove(file)
            print("- removed!")
            # - Write to the log:
            event_message = 'Detected, uploaded and removed file ' + file
            log_event(reporting_program_name, event_message)
        except Exception as error_message:
            log_error(reporting_program_name, error_message)
            print("- failed. Check the error.log")
    time.sleep(1)
