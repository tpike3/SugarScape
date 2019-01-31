# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 06:09:24 2018

@author: ymamo
"""



import NetAgent as N



def survivors(model):
    
    alive =  model.ml.active_agent_count
    
    return alive

def get_agent_health(model):
    
    for k,v in model.ml.agents_by_type[N.NetAgent].items():
        model.datacollector.add_table_row("Health", {"Agent":v.unique_id, \
                                          "Sugar_Level": v.accumulations[1], \
                                          "Spice_Level": v.accumulations[2], \
                                          "Step": model.step_num})
    
def get_time(model,time):
    model.datacollector.add_table_row("Time", {"Time Per Step": time})
    
def get_price(model):
    
    for k,v in model.ml.agents_by_type[N.NetAgent].items():
        model.price_record[model.step_num][k] = v.price
        
    