# - motion_detect():
import RPi.GPIO as GPIO
import time, datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  # PIR sensor
GPIO.setup(13, GPIO.IN)  # Button
GPIO.setup(15, GPIO.OUT) # LED

# - PiCamera:
from picamera import PiCamera

# - Loggers:
from loggers import log_event, log_error 

# - File upload:
import os
import boto3
from botocore.exceptions import ClientError


def flash_led(flashes=3):
    for i in range(flashes):
        GPIO.output(15,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(15,GPIO.LOW)
    time.sleep(0.5)


def confirm_button_press():
    confirm_press_bool = False
    # - if the button is pressed, wait for 3 seconds and then check it again.
    # - if still pressed -> transition to state 2 (arming)
    GPIO.output(15,GPIO.HIGH) # Turn LED on
    time.sleep(3)
    GPIO.output(15,GPIO.LOW) # Turn LED off
    button_state = GPIO.input(13)
    if button_state == True:
        # - LED flassing:
        flash_led(flashes=5)
        # - confirm the press:
        confirm_press_bool = True
    else:
        pass 
    return confirm_press_bool


def read_button(arm_state):
    if arm_state == 1:
        button_state = GPIO.input(13) 
        if button_state == True:
            print(confirm_button_press())
            arm_state = 1
        else:
            pass
        
    elif arm_state == 2:
        pass
        
    elif arm_state == 3:
        pass
        
    return arm_state





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
        camera.resolution = (1024, 768)
        camera.start_preview()
        file_name = './media/video_{}h_{}s.h264'.format(st, video_lenght)
        camera.start_recording(file_name)
        time.sleep(video_lenght)
        camera.stop_recording()
        camera.stop_preview()
        camera.close()
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