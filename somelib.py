import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def func():
    log.critical('A Critical error!')
    log.debug('a debug message')