import functions
import time
from loggers import log_error, log_event

reporting_program_name = 'rpi_home_guardian.py'
event_message = 'Starting program'
log_event(reporting_program_name, event_message)

# - Read initial state (1=unarmed, 2=arming, 3=armed):
arm_state = 1

functions.flash_led(flashes=20)

while True:
    # - UNARMED:
    if arm_state == 1:
        # - Change the state if the burron is pressed:
        arm_state = functions.read_button(arm_state)
        
        
    
    # - ARMING:
    elif arm_state == 2:
        time.sleep(5)
        arm_state = 3

    # - ARMED:
    elif arm_state == 3:
        # - Check for files ./media and upload them:
        functions.check_upload_files()

        # - Detect motion:
        motion_bool = functions.motion_detect()
        if motion_bool == True:
            functions.take_video(5)
        else:
            time.sleep(1)
    
    time.sleep(0.1)