#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 5/2014
#   Title: SUBTASK
#   Description: Todo list manager with subtasks
#   License:
import os
import uuid
import json
from datetime import datetime
from subtask.config import Configuration
from subtask.task import Task

def jdefault(o):
    return o.__dict__

def main(cmd_args):
    """ Configure settings from command line """
    config_settings = Configuration()

    tasks = Task("root")

#    tasks.add_task("Task One")
#    tasks.add_task("Task Two x")
#    tasks.add_task("Task Three")
#    sta = tasks.search_by_description("One")
#    sta[0].add_task("Task One Bird")

#    asta = tasks.search_by_description("Bird")
#    print(json.dumps(asta, default=jdefault))

    if cmd_args['add']:
        cmd_args['<text>'] = ' '.join(cmd_args['<text>'])
        if cmd_args['<filter>']:
            print("st filter add")
        else:
            tasks.add_task(cmd_args['<text>'])
       
    dog = json.dumps(tasks)
    print(json.loads(dog))
#with open('data.txt', 'w') as outfile:
#    outfile.write(json.dumps(projects, default=jdefault))
            #json.dumps(new_task, default=jdefault, outfile)

##    elif cmd_args['note']:
#        cmd_args['<text>'] = ' '.join(cmd_args['<text>'])
#        note = Note(cmd_args['<text>'], uuid.uuid1(), 'pending', datetime.now(), int(1))
#        s.add_all([note])
#        s.commit()
#        for note in s.query(Note):
#            print(type(note), note.note)
#    elif ((cmd_args['delete'] or cmd_args['done'] or cmd_args['edit'] or cmd_args['revive']) and 
#            cmd_args['<filter>'] != None):
#        print("Only in here if one of the options and a filter is set.")
#    else:
#        print("Print all with filter or not")
