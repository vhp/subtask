#!/usr/bin/env python3
#
#   Author: Vincent Perricone <vhp@fastmail.fm>
#   Date: 5/2014
#   Title: SUBTASK
#   Description: Todo list manager with subtasks
#   License:
"""
Usage:
    st
    st [<filter>]
    st add <text>...
    st (<filter>) add <text>...
    st (<filter>) note <text>...
    st (<filter>) done
    st (<filter>) delete
    st (<filter>) edit
    st (<filter>) revive
    st (-h | --help)
    st (-V | --version)

Options:
  -h, --help
  -V, --version

"""

import sys
from subtask import subtask
from subtask.docopt import docopt

__version__ = 'Subtask 0.1'

if __name__ == '__main__':
    command_args = docopt(__doc__, version = __version__)
    sys.exit(subtask.main(command_args))
