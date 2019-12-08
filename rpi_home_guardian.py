import functions
import time
from loggers import log_error, log_event

reporting_program_name = 'rpi_home_guardian.py'
event_message = 'Starting program'
log_event(reporting_program_name, event_message)

# - Read initial state (1=unarmed, 2=arming, 3=armed):
arm_state = 1

# - Arming time (sec)
arming_time = 20


while True:
    # - UNARMED:
    if arm_state == 1:
        # - Got to arming if the button is pressed for 3 sec:
        arm_state = functions.read_button(arm_state)
        
        # - Flash 1 time to indicate state is UNARMED:
        functions.flash_led(flashes=1)
        # - Delay:
        time.sleep(0.9)
    
    
    # - ARMING:
    elif arm_state == 2:
        # - Delay arming_time seconds than go to state armed:
        for i in range(arming_time):
            functions.flash_led(flashes=2)
            time.sleep(0.8)
        # - Record UNAMED -> ARMING in the event log:
        reporting_program_name = 'rpi_home_guardian.py'
        event_message = '{}s pressed. Home guardian ARMED'.format(arming_time)
        log_event(reporting_program_name, event_message)
        arm_state = 3

        
    # - ARMED:
    elif arm_state == 3:
        # - Disarm if the button is pressed for 3 sec:
        arm_state = functions.read_button(arm_state)
    
        '''
        # - Check for files ./media and upload them:
        functions.check_upload_files()

        # - Detect motion:
        motion_bool = functions.motion_detect()
        if motion_bool == True:
            functions.take_video(5)
        else:
            pass
        '''
        
        # - Flash 3 times to indicate state is ARMED:
        functions.flash_led(flashes=3)
        # - Delay:
        time.sleep(0.7)