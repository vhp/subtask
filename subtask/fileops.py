#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 5/2014
#   Title: SUBTASK
#   Description: Todo list manager with subtasks
#   License: Released under "Simplified BSD License" see LICENSE file
import os
import json

def write_db(config_settings, data):
    db = (os.path.expanduser('{0}{1}'.format(
                config_settings.settings['db.directory'],
                config_settings.settings['db.database'])))
    with open(db, 'w') as json_db:
        json_db.write(data)

def read_db(config_settings):
    db = (os.path.expanduser('{0}{1}'.format(
                config_settings.settings['db.directory'],
                config_settings.settings['db.database'])))
    with open(db, 'r') as json_db:
        try:
            data = json.load(json_db)
            return data
        except ValueError:
            return None
