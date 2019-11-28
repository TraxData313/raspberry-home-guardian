import os
import time
from time import sleep
#import logging
#import boto3
#from botocore.exceptions import ClientError





print()
print()
print()
print('Starting program...')

# - Initialize variables:
files = []
filesExistBool = 0


# - Recover the bucket name from the settings file:
bucket_name = open('settings.txt', 'r').readlines()
bucket_name = str(bucket_name[1])
bucket_name = bucket_name[:-1]
print()
print("S3 bucket name is", bucket_name)




while True:
    print()
    print()
    print()
    
    # - Check for files:
    print()
    print("Looking for files in ./media...")
    del files
    files = os.listdir(".\media")
    for file in files:
        print()
        print("Found file:", file)
        # - Rename the file (add the path to it):
        file =  "./media/" + file
        
        # - Upload the file to the S3 bucket:
        print()
        print("Uploading the file to S3...")
        try:
            upload_file(file_name=file, bucket=bucket_name)
            print("Done!")
            # - Remove the file:
            print()
            print("Removing the file from ./media...")
            os.remove(file)
            print("Done!")
        except:
            print("Failed!")
        
    time.sleep(1)


    
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True