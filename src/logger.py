import logging

#
# init_logger() - setup logger (debug messages and stuff...)
#
def init(level):
    logobj = logging.getLogger()
    # if level == 'DEBUG':
    #     logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    #     print "> Debug level: DEBUG"
    # elif level == 'INFO':
    #     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    #     print "> Debug level: INFO"        
    # else:
    #     logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    if level == 'DEBUG':
        logging.basicConfig(level=logging.DEBUG, format='> %(levelname)s: %(message)s')
        print "> Debug level: DEBUG"
    elif level == 'INFO':
        logging.basicConfig(level=logging.INFO, format='> %(levelname)s: %(message)s')
        print "> Debug level: INFO"        
    elif level == 'WARNING':
        logging.basicConfig(level=logging.WARNING, format='> %(levelname)s: %(message)s')
        print "> Debug level: WARN"        
    else:
        logging.basicConfig(level=logging.ERROR, format='> %(levelname)s: %(message)s')

    return logobj