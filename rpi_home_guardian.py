import functions
import time


while True:
    # - Check for files ./media and upload them:
    functions.check_upload_files()

    # - Detect motion:
    motion_bool = functions.motion_detect()
    if motion_bool == True:
        functions.take_video(5)
    else:
        time.sleep(1)