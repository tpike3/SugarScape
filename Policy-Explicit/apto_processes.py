# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 08:59:32 2018

@author: ymamo
"""
#import NetAgent as N

def form_connection_group(model):
        
    for agent, trades in model.trades.items():
        #Must pass in agent
        agents = [agent]
        for partner, num_trades in trades.items():
            if num_trades >= 10:              
                agents.append(partner)
        
        if len(agents)  > 1: 
            yield agents
            
        else:
            pass
            
            
def reassess(meta_agent): 
    
     for k,v in meta_agent.sub_agents.items(): 
         if v.type == "agent" and v.pos not in meta_agent.sub_agents.keys():
             return meta_agent.sub_agents.values()
             