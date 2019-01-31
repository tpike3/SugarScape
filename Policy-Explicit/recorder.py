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
                                          "Spice_Level": v.accumulations[2], 
                                          "Step": model.step_num})
    
def get_time(model,time):
    model.datacollector.add_table_row("Time", {"Time Per Step": time})
    
def get_price(model):
    price_record = {}
    for k,v in model.ml.agents_by_type[N.NetAgent].items():
        price_record[k] = v.price
        
    return price_record

def get_meta_details(model):
    
    meta_list = []
    independents = 0
    for k, meta in model.ml.schedule.items(): 
        if meta.type == "resource":
                pass
        elif meta.type == "agent":
                independents += 1 
        elif meta.type == 'meta':
            if meta.policy != None:
                meta_list.append([meta.unique_id, meta.policy.policy_type, \
                                  len(meta.sub_agents)])
            else: 
                meta_list.append([meta.unique_id, len(meta.sub_agents)])
                       
        
    model.meta_type[model.step_num] = [meta_list, independents]