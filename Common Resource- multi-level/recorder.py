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
        
def get_meta_details(model):
    
    meta_list = []
    independents = 0
    for k, meta in model.ml.schedule.items(): 
        if meta.type == "resource":
                pass
        elif meta.type == "agent":
                independents += 1 
        elif meta.type == 'meta':
            metas= 0
            agnts = 0
            for sub in meta.sub_agents.values(): 
                if sub.type == "meta":
                    metas += 1
                else: 
                    agnts += 1
            meta_list.append([agnts, metas])
                       
        
    model.meta_type[model.step_num] = [meta_list, independents]

def agent_iter(agents, storage):
       
       for agent_id, agent in agents.sub_agents.items(): 
           if agent.type == 'meta':
               storage.append(agent_id)
               agent_iter(agent, storage)
           else:
               storage.append(agent_id)
       return storage

def get_final(model_items, agent_dict, k):
    
    for sub_id, agents in model_items:
        if agents.type == "resource":
            pass
        elif agents.type == "group": 
            agent_dict[sub_id] = get_final(agents.sub_agents.items(), {sub_id:[]}, sub_id)
        else: 
            agent_dict[k].append(sub_id)
    return agent_dict
                

        
    