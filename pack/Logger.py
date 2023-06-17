# Jake Prisby

# Desc.: This file handles all interactions with the log files

import logging

# Desc.: Logger object
class Logger():

    # Desc.: Constructor for logger object
    # Input: level - Logging level
    def __init__(self, level= logging.INFO):
        # Generate file name
        from datetime import datetime
        self.start_time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        # Create log file
        file_name = 'Log_'+ self.start_time + '.log'
        import os
        # Create log folder if it does not exist
        if not os.path.exists('Logs\\'):
            os.mkdir('Logs\\')
        # Create log file
        logging.basicConfig(filename= 'Logs\\' + file_name,
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(level)

    # Desc.: Write a debug level message to the log file
    # Input: Message being written to log
    def write_debug(self, msg):
        self.logger.debug(str(msg))

    # Desc.: Write a info level message to the log file
    # Input: Message being written to log
    def write_info(self, msg):
        self.logger.info(str(msg))

    # Desc.: Write a warning level message to the log file
    # Input: Message being written to log
    def write_warning(self, msg):
        self.logger.warning(str(msg))

    # Desc.: Write a error level message to the log file
    # Input: Message being written to log
    def write_error(self, msg):
        self.logger.error(str(msg))

    # Desc.: Write a critical level message to the log file
    # Input: Message being written to log
    def write_critical(self, msg):
        self.logger.critical(str(msg))