import logging
import logging.config

def main():
    # configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR # any level below will be ignored
    )

    # using a config file
    logging.config.fileConfig('logconfig.ini')

    # variables
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'   
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()