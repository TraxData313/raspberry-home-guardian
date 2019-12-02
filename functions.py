# - motion_detect():
import RPi.GPIO as GPIO
import time, datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

# - PiCamera:
from picamera import PiCamera

# - Loggers:
import loggers


def motion_detect():
    """Check if the PIR sensor attached at BOARD port 11 is detecting motion and returns True or False
    """
    return GPIO.input(11)


def take_video(video_lenght=5):
    reporting_program_name = 'functions.take_video'
    # - Get the current time:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H%M%S')
    # - Record the video:
    try:
        camera = PiCamera()
        camera.start_preview()
        file_name = './media/video_{}s_{}h.h264'.format(video_lenght, st)
        camera.start_recording(file_name)
        time.sleep(video_lenght)
        camera.stop_recording()
        camera.stop_preview()
        # - Log event:
        event_message = 'Created video {}'.format(file_name)
        loggers.log_event(reporting_program_name, event_message)
    except Exception as error_message:
        # - Log error:
        loggers.log_error(reporting_program_name, error_message)

