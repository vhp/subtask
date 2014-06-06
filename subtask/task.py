#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 1/2014
#   Title: SUBTASK
#   Description: Todo task manager with subtasks
#   License:
#
import uuid
import json
from datetime import datetime

class Task:

    def __init__(self, description):
        self.uuid = None
        self.description = description
        self.status = None
        self.timestamp = None
        self.children = []
        self.set_uuid()
        self.set_timestamp()
        self.set_status()

    def dump_tasks(self):
        """Dump tasks for this object"""
        return {'uuid': self.uuid,
                'description': self.description,
                'status':   self.status,
                'timestamp': self.timestamp,
                'children': [child_task.dump_tasks() for child_task in self.children]}

    @classmethod
    def load_tasks(cls, json_dict):
        """Recreate instances of Task"""
        node = cls(json_dict['description'])
        node.uuid = json_dict['uuid']
        node.status = json_dict['status']
        node.timestamp = json_dict['timestamp']
        for child in json_dict['children']:
            node.children.append(cls.load_tasks(child))
        return node

    def add_task(self, description):
        """Add new child task object to child list"""
        task_obj = Task(description)
        self.children.append(task_obj)

    def set_uuid(self):
        """set uuid of self task"""
        if self.uuid == None:
            self.uuid = str(uuid.uuid1())

    def set_status(self):
        """set task status of self"""
        if self.status == None:
            self.status = 'pending'

    def set_timestamp(self):
        """set creation stamp of task"""
        if self.timestamp == None:
            self.timestamp = str(datetime.now())

    def walk_tree(self, task):
        """Walk tree generator"""
        yield task
        for child in task.children:
            for grandchild in self.walk_tree(child):
                yield grandchild

    def days_old(self, dates):
        days = (datetime.today() - datetime.strptime(dates, '%Y-%m-%d %H:%M:%S.%f')).days
        if days <= 7:
            return '{0}d'.format(round(days, 1))
        elif days >=7:
            return '{0}w'.format(round(days/7, 1))

    def print_node(self, prefix):
        print('{0}   {1} {2} {3}'.format(self.days_old(self.timestamp), self.status, prefix, self.description))
        for child in self.children:
            child.print_node("    ")

    def printer(self):
        """Search task hierarchy by description field"""
        for task in self.walk_tree(self):
            print('{0} {1} {2}'.format(task.status, task.timestamp, task.description))

    def search_by_description(self, query):
        """Search task hierarchy by description field"""
        found_tasks = []
        for task in self.walk_tree(self):
            if query in task.description:
                found_tasks.append(task)
        return found_tasks

    def get_me(self):
        """Search task hierarchy by description field"""
        return (self.timestamp, self.status, self.description)
