# - motion_detect():
import RPi.GPIO as GPIO
import time, datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

# - PiCamera:
from picamera import PiCamera

# - Loggers:
from loggers import log_event, log_error 

# - File upload:
import os
import boto3
from botocore.exceptions import ClientError


def motion_detect():
    """Check if the PIR sensor attached at BOARD port 11 is detecting motion and returns True or False
    """
    return GPIO.input(11)


def take_video(video_lenght=5):
    """Takes video of lenght=video_lenght in seconds,
    and saves it in ./media
    """
    reporting_program_name = 'functions.take_video'
    # - Get the current time:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    # - Record the video:
    try:
        camera = PiCamera()
        camera.start_preview()
        file_name = './media/video_{}h_{}s.h264'.format(video_lenght, st)
        camera.start_recording(file_name)
        time.sleep(video_lenght)
        camera.stop_recording()
        camera.stop_preview()
        # - Log event:
        event_message = 'Created video {}'.format(file_name)
        log_event(reporting_program_name, event_message)
    except Exception as error_message:
        # - Log error:
        log_error(reporting_program_name, error_message)


# - Function that upoads files to S3:
def upload_file(file_name, bucket, object_name=None):
    # - Initialize variables:
    reporting_program_name = 'functions.check_upload_files.upload_file.py'
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


def check_upload_files():
    """Looks for files in ./media, 
    if found -> uploads them to S3 and deltes them after
    """
    # - Initialize variables:
    reporting_program_name = 'functions.check_upload_files.py'

    # - Recover the bucket name from the settings file:
    bucket_name = open('settings.txt', 'r').readlines()
    bucket_name = str(bucket_name[1])
    bucket_name = bucket_name[:-1]
    
    # - Check for files:
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