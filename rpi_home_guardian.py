import functions
import time
import os
from loggers import log_error, log_event

# - Log starting event:
reporting_program_name = 'rpi_home_guardian.py'
event_message = 'Home guardian booting up'
log_event(reporting_program_name, event_message)

# - Read initial state (1=unarmed, 2=arming, 3=armed):
arm_state = 3 # Defaults to ARMED
state_file = 'arm_state.txt'
if not os.path.exists(state_file):
    print('- No arm_state file, creating...')
    functions.save_state(state_file, arm_state)
    print("-- Done!")
else:
    try:
        arm_state = functions.read_state(state_file)
    except Exception as error_message:
        log_error(reporting_program_name, error_message)
        print("- Failed to load the arm_state. Removing the file...")
        os.remove(state_file)
        arm_state = 3
        event_message = 'Error handeled. Removed the corrupted arm_state file. State set to ARMED'
        print(event_message)
        log_event(reporting_program_name, event_message)
    
# - Log the state in the events:
reporting_program_name = 'rpi_home_guardian.py'
event_message = 'STATE is {} (1=unarmed, 2=arming, 3=armed)'.format(arm_state)
log_event(reporting_program_name, event_message)

# - Arming time (sec)
arming_time = 20


while True:
    # - UNARMED:
    if arm_state == 1:
        # - Got to arming if the button is pressed for 3 sec:
        arm_state = functions.read_button_and_change_state(arm_state, state_file)
        
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
        event_message = '{}s or arming passed. Home guardian ARMED'.format(arming_time)
        log_event(reporting_program_name, event_message)
        arm_state = 3
        # - Record the state to the file:
        functions.save_state(state_file, arm_state)

        
    # - ARMED:
    elif arm_state == 3:
        # - Disarm if the button is pressed for 3 sec:
        arm_state = functions.read_button_and_change_state(arm_state, state_file)
    
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
        
        
    # - STATE is corrupted error:
    else:
        reporting_program_name = 'rpi_home_guardian.py'
        error_message = 'State is CORRUPTED. Not equil to 1,2 or 3, or the file is illformated. Delete {} and rerun the program!'.format(state_file)
        log_error(reporting_program_name, error_message)
        break