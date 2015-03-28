#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 5/2014
#   Title: SUBTASK
#   Description: Todo list manager with subtasks
#   License:
import json
from subtask.config import Configuration
from subtask.task import Task
from subtask.fileops import write_db, read_db


def main(cmd_args):
    """Configure settings from command line"""
    config_settings = Configuration()
    cmd_args['<text>'] = ' '.join(cmd_args['<text>'])

    json_data = read_db(config_settings)
    if isinstance(json_data, dict):
        root_task = Task.load_tasks(json_data)
    else:
        root_task = Task("root")

    if cmd_args['add']:
        if cmd_args['<filter>']:
            found_task = root_task.search(cmd_args['<filter>'])
            found_task.add_task(Task(cmd_args['<text>']))
        else:
            root_task.add_task(Task(cmd_args['<text>']))
    elif cmd_args['delete']:
        if cmd_args['<filter>']:
            found_task = root_task.search(cmd_args['<filter>'])
            if len(found_task.children) > 0:
                print("This task has children.  You don't want to delete it")
            else:
                print('Deleting')
                del found_task
        else:
            print('You must operate on a task')
    else:
        root_task.print_all(root_task)

#Clean up and write
    if len(root_task.children) > 0:
        write_db(config_settings, json.dumps(root_task.dump_tasks(), sort_keys=False, indent=4))
