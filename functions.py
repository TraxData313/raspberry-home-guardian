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
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H.%M.%S')
    # - Record the video:
    try:
        camera = PiCamera()
        camera.start_preview()
        camera.start_recording('./media/video.{}s.{}.h256'.format(video_lenght, st))
        time.sleep(video_lenght)
        camera.stop_recording()
        camera.stop_preview()
    except Exception as error_message:
        loggers.log_error(reporting_program_name, error_message)
    # - Log the event:
    event_message = 'Created video ./media/video.{}.{}.h256'.format(video_lenght, st)
    loggers.log_event(reporting_program_name, event_message)
