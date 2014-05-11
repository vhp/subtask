#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 1/2014
#   Title: SUBTASK
#   Description: Todo task manager with subtasks
#   License:
#


class List():

    def __init__(self):
        self.task_tree = Task(None, "root")

    def find_parent(self, ):

    def create_task(self, parent, description):
        """Create new Task object""" 
        task_obj = Task(parent, description)
        self.add_task(task_obj)







#    def walk_tree(task)
#        yield task
#        for child in task.children:
#            for grandchild in walk(child):
#                yield grandchild
###This doesn't work yet.  
#    def search_description(self, query):
#        for task in walk_tree(self.tasklist[0]):
#            if query in if task.description:

            
