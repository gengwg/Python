from configparser import ConfigParser

cfg = ConfigParser()
print(cfg.read('config.ini'))
print(cfg.sections())
# names used in a config file are case-insensitive
print(cfg.get('installation', 'library'))
print(cfg.get('installation', 'LIBRARY'))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.get('debug', 'log_errors'))
print(cfg.getint('server', 'port'))
print(cfg.getint('server', 'nworkers'))
print(cfg.get('server', 'signature'))

# variable interpolation is performed as late as possible
cfg.set('installation', 'prefix', '/tmp/dir')
print(cfg.get('installation', 'library'))

# modify the config file and write it back to a file
cfg.set('server', 'port', '9000')
cfg.set('debug', 'log_errors', 'False')
import sys
cfg.write(sys.stdout)