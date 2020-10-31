#! /usr/bin/env python3.8

# modules

# package is a directory of python files with that contains __init__.py file
# __init__.py file can be empty, just indicates package structure

# import looks through module path and import path, gives name in local namespace

import math

from math import *

import mypackage.mymodule as myModule

print  (myModule.myAdd(1, 3))
