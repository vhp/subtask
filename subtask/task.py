#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 1/2014
#   Title: SUBTASK
#   Description: Todo task manager with subtasks
#   License:
#
import uuid

class Task():

    def __init__(self, description):
        self.uuid = None
        self.description = description
        self.status = None
        self.timestamp = None
        self.set_uuid()
        self.children = []

    def add_task(self, description):
        """Add child task object to list"""
        task_obj = Task(description)
        self.children.append(task_obj)

    def set_uuid(self):
        """set uuid of task"""
        if self.uuid == None:
            self.uuid = uuid.uuid1()

    def walk_tree(self, task):
        yield task
        for child in task.children:
            for grandchild in self.walk_tree(child):
                yield grandchild

    def search_by_description(self, query):
        found_tasks = []
        for task in self.walk_tree(self):
            if query in task.description:
                found_tasks.append(task)
        return found_tasks

