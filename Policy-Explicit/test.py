# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 06:00:22 2018

@author: ymamo
"""


from itertools import groupby

test = ["A", "B", "C"]
test.remove(test[0])
test2 = "A"*len(test)
print (test2)
new = list(zip(test2, test))

print (new)
