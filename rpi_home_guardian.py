import functions
import time
from loggers import log_error, log_event

reporting_program_name = 'rpi_home_guardian.py'
event_message = 'Starting program'
log_event(reporting_program_name, event_message)

while True:
    # - Check for files ./media and upload them:
    functions.check_upload_files()

    # - Detect motion:
    motion_bool = functions.motion_detect()
    if motion_bool == True:
        functions.take_video(5)
    else:
        time.sleep(1)