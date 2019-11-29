import logging
import time, datetime, os


# - Function that logs error messages:
def log_error(program, message):
    """Creates an error in ./logs/error.log
    """
    print()
    print("Loggind error...")

    # - Create log dir if it doesn't exist:
    if not os.path.exists('logs'):
        print('- No log directory, creating...')
        os.mkdir('./logs');
        print("-- Done!")
    else:
        pass


    # - Get current time:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    # - Append an error:
    appendFile = open('logs/error.log', 'a')
    appendFile.write('\n')
    appendFile.write(st)
    appendFile.write(' ')
    appendFile.write(program)
    appendFile.write(': ')
    appendFile.write(message)


    appendFile.close()


    print("- Done!")
    print()