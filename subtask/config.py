#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 5/2014
#   Title: SUBTASK
#   Description: Todo list manager with subtasks
#   License:
import os
import sys
try:
    import configparser
except ImportError:
        print('Module configparser Not loaded')
        sys.exit(1)

class Configuration:
    """Class handling state of configuration"""
    def __init__(self):
        """Configuration Constructor: Set stuff up"""
        self.configfile = '~/.subtask.rc'
        self.settings = {'db.directory': '~/.subtask/', 
                        'db.database': 'subtask.db'}
        self.create()
        self.load_config()

    def load_config(self):
        """Read configuration file from system"""
        try:
            with open(os.path.expanduser(self.configfile)) as conf: pass
        except IOError:
            print('Config {0} does not exist'.format(self.configfile))
        else:
            config = configparser.ConfigParser()
            config.read(os.path.expanduser(self.configfile))
            for key, value in dict(config.items('subtask')).items():
                if not self.settings[key] in value:
                    self.settings[key] = value

    def write_config(self, open_conf_obj):
        """Write out configuration to previously open file object"""
        config = configparser.ConfigParser()
        config.add_section('subtask')
        for option, value in self.settings.items():
            print(option, value)
            config.set('subtask', option, value )
        config.write(open_conf_obj)
        print('New Config file written')

    def create(self):
        """ Create config file if it doesn't already exist.
            Call write_config() to actually write configuration to file object
        """
        config = os.path.expanduser(self.configfile)
        try:
            user_config_obj = open(config, 'r')
        except (OSError, IOError):
            print('Config file does not exist')
            try:
                user_config_obj = open(config, 'w')
            except IOError:
                print('{0} could not be open for writing'.format(config))
            else:
                self.write_config(user_config_obj)
        finally:
            user_config_obj.close()

