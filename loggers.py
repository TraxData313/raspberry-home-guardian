import time, datetime, os


'''
USAGE with example:

- Place this file in the directory of your python code and
  in the code import the module by:
# import loggers

- Define the reporting_program_name at the beggining of your program,
  when you have to log and error or an event, set the message you want to report in
# error_message = "your error here" or event_message = "your event here"

  and use the loggers as follows:
# log_error(reporting_program_name, error_message)
# log_event(reporting_program_name, event_message)

- The messages get created in:
./logs/error.log and events.log

- Here is how the logs will appear:
2019-11-29 12:25:36 reporting_program_name [ERROR]: your error here
2019-11-29 12:25:36 reporting_program_name [EVENT]: your event here
'''


# - Function that logs error messages:
def log_error(reporting_program_name, error_message):
    """Adds entry in ./logs/error.log,

    where the reporting program = reporting_program_name
    and the error_message = error_message
    """
    # - Create log dir if it doesn't exist:
    if not os.path.exists('logs'):
        print('- No log directory, creating...')
        os.mkdir('./logs');
        print("-- Done!")
    else:
        pass
    # - Get the current time:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # - Append an error:
    appendFile = open('logs/error.log', 'a')
    appendFile.write('\n')
    appendFile.write(st)
    appendFile.write(' ')
    appendFile.write(reporting_program_name)
    appendFile.write(' [ERROR]: ')
    appendFile.write(error_message)
    appendFile.close()


# - Function that logs error messages:
def log_event(reporting_program_name, event_message):
    """Adds entry in ./logs/event.log,

    where the reporting program = reporting_program_name
    and the event_message = event_message
    """
    # - Create log dir if it doesn't exist:
    if not os.path.exists('logs'):
        print('- No log directory, creating...')
        os.mkdir('./logs');
        print("-- Done!")
    else:
        pass
    # - Get the current time:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # - Append an event:
    appendFile = open('logs/events.log', 'a')
    appendFile.write('\n')
    appendFile.write(st)
    appendFile.write(' ')
    appendFile.write(reporting_program_name)
    appendFile.write(' [EVENT]: ')
    appendFile.write(event_message)
    appendFile.close()