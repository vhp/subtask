#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 1/2014
#   Title: SUBTASK
#   Description: Todo task manager with subtasks
#   License: Released under "Simplified BSD License" see LICENSE file
#
import uuid
import json
import re
from datetime import datetime

class Task:

    def __init__(self, description):
        self.uuid = None
        self.description = description
        self.status = None
        self.timestamp = None
        self.children = []
        #Node setup
        self.set_uuid()
        self.set_timestamp()
        self.set_status()

    def dump_tasks(self):
        """Dump tasks for this object"""
        return {'uuid': self.uuid,
                'description': self.description,
                'status':   self.status,
                'timestamp': str(self.timestamp),
                'children': [child_task.dump_tasks() for child_task in self.children]}

    @classmethod
    def load_tasks(cls, json_dict):
        """Recreate instances of Task"""
        node = cls(json_dict['description'])
        node.uuid = json_dict['uuid']
        node.status = json_dict['status']
        node.timestamp = datetime.strptime(json_dict['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        for child in json_dict['children']:
            node.children.append(cls.load_tasks(child))
        return node

    def set_uuid(self):
        """set uuid of self task"""
        if self.uuid == None:
            self.uuid = str(uuid.uuid1())

    def set_status(self):
        """set task status of self"""
        if self.status == None:
            self.status = 'p'

    def set_timestamp(self):
        """set creation stamp of task"""
        if self.timestamp == None:
            self.timestamp = datetime.now()

    def add_task(self, child):
        """Take child task object as parameter and append to list children"""
        self.children.append(child)

    def delete_task(self):
        if len(self.children) > 0:
            print("This task has children.  You don't want to delete it")
        else:
            print('Deleting')
            del self

    def walk_tree(self, task):
        """Walk tree generator"""
        yield task
        for child in task.children:
            for grandchild in self.walk_tree(child):
                yield grandchild

    def get_me(self):
        """Search task hierarchy by description field"""
        return (self.timestamp, self.status, self.description)

    def search_by_description(self, query):
        """Search task hierarchy by description field"""
        found_tasks = []
        for task in self.walk_tree(self):
            if query in task.description:
                found_tasks.append(task)
        if len(found_tasks) > 1:
            print("Multiple entries found in search, be more specific")
            sys.exit()
        else:
            return found_tasks

    def fetch_node(self, index):
        """Return node (self) or specific index if specified"""
        if len(self.children) == 0:
            return self
        elif (index >= 0 and index < len(self.children)):
            return self.children[index]
        else:
            raise ValueError('Node unfortunately does not exist.')

    def search(self, query):
        """Search task tree, verify if query matches node pattern"""
        pattern = '^(\d+)(\.(\d+))*$'
        if re.match(pattern, query):
            node = self
            for i in map(lambda j: int(j) - 1 , query.split('.')):
                node = node.fetch_node(i)
            return node
        else:
            print('else')
            return self.search_by_description(query)

#Printer
    def days_old(self, date):
        days = (datetime.today() - date).days
        if days <= 7:
            return '{0}d'.format(round(days, 1))
        elif days >=7:
            return '{0}w'.format(round(days/7, 1))

    def print_all(self, referring_node, task_num='1', indent=''):
        """Print task Hierachy"""
        if self.description not in 'root':
            #print(': '.join([task_num, self.description]))
            print('{0} ({1})({2}): {3}'.format(task_num, self.status, self.days_old(self.timestamp), self.description))
        for index, child in enumerate(self.children, 1):
            if referring_node.description in 'root':
                child.print_all(child, ''.join((indent, str(index))),'    ')
            else:
                child.print_all(child, ''.join((indent, task_num, '.', str(index))),'    ')

