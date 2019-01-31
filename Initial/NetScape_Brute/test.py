# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 06:00:22 2018

@author: ymamo
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import pkgutil
search_path = None# set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)