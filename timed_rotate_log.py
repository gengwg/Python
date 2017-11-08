# Rotate the logs based on some time interval (TimedRotatingFileHandler)
# https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/
#
# backupCount in number of old log files to keep
#
# Current 'when' events supported:
#   S - Seconds
#   M - Minutes
#   H - Hours
#   D - Days
#   midnight - roll over at midnight
#   W{0-6} - roll over on a certain day; 0 - Monday
#
# Case of the 'when' specifier is not important; lower or upper case
# will work.
#
# Roll over at midnight:
#   when=''midnight

import logging
import time

from logging.handlers import TimedRotatingFileHandler

#----------------------------------------------------------------------
def create_timed_rotating_log(path):
    """"""
    #logger = logging.getLogger("Rotating Log")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(path,
                                       when="m",    # minute
                                       interval=1,
                                       backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    for i in range(6):
        logger.info("This is a test!")
        time.sleep(75)

#----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "timed_test.log"
    create_timed_rotating_log(log_file)
