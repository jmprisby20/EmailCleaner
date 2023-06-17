# Jake Prisby

# Desc.: This file handles interactions between the program and the config.ini file 

from configparser import ConfigParser

# Desc.: Config file handler object
class ConfigManager():

    # Desc.: CofigManager Constructor 
    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('config.ini')

    # Desc.: Set a given value in the config file
    # Input: section - Section of the config file
    #        path - Variable name
    #        val - Value being written for variable
    def set_val(self,section, path, val):
        self.parser.set(section, path, val)
        with open('config.ini', 'w') as configfile:
            self.parser.write(configfile)
            
    # Desc.: Get a given value from the config file
    # Input: section - Section value is stored in
    #        path - Name of variable
    # Output: Value stored in ini at given location
    def get_val(self, section, path):
        return self.parser.get(section, path)
