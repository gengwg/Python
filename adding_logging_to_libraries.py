import somelib
# null handler igonres all messages. so no output here.
somelib.func()

# logging system gets configured. log messages will appear.
import logging
logging.basicConfig()
somelib.func()

# change logging settings for single module 'somelib'
logging.getLogger('somelib').level=logging.DEBUG
somelib.func()

