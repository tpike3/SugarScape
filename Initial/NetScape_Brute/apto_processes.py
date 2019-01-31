# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 08:59:32 2018

@author: ymamo
"""

import NetAgent as N
import ResourceScape as R

def form_connection(model):
    
    for agent in model.ml.agents_by_type[N.NetAgent].values():
        meta = []
        meta.append(agent)
        meta.append(model.ml.agents_by_type[R.resource][agent.pos])
        yield meta
    
def reassess(meta): 
     
   resource = list(meta.subs_by_type[R.resource].values())
   agent = list(meta.subs_by_type[N.NetAgent].values())
   if resource[0].pos != agent[0].pos:
       return [resource[0], agent[0]]    
          