# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 05:41:06 2019

@author: ymamo
"""

from random import randint
from scipy.stats.mstats import gmean
#from ML_Mesa import MetaAgent

class rules(): 
    
    def __init__(self): 
        self.policy_type = self.choose_type()
    
    def choose_type(self):
        policy = randint(1,3)
        
        if policy == 1: 
            return "low focus"
        if policy == 2: 
            return "high focus"
        if policy ==3: 
            return "aggregate"
    
    def step_low(self, agent, meta):
        
        lowest = None
        sele_agent = None
        
        
        #identify the lowest
        for status in meta.sub_agents.values(): 
            if lowest == None: 
                lowest = list(status.accumulations.values())
                sele_agent = status.unique_id
            else:
                new = list(status.accumulations.values())
                if min(lowest) > min(new):
                    lowest = new
                    sele_agent = status.unique_id
        
        psuedo_accs = meta.sub_agents[sele_agent].accumulations
        
        #for agent in meta.agent_buffer(): 
        #store actual
        actual = agent.accumulations
        #replcae your accumulations with those of the lowest
        agent.accumulations = psuedo_accs
        #move with this new percpetion
        agent.move()
        #return you accumulations
        agent.accumulations = actual
        agent.eat()
        agent.die()
        if agent.status == "dead":
            return
        agent.trade()
                    
    def step_high(self, agent,meta):
        
        highest = None
        sele_agent = None
        
        #identify the highest
        for status in meta.sub_agents.values(): 
            if highest == None: 
                highest = list(status.accumulations.values())
                sele_agent = status.unique_id
            else:
                new = list(status.accumulations.values())
                if max(highest) > max(new):
                    highest = new
                    sele_agent = status.unique_id
        
        psuedo_accs = meta.sub_agents[sele_agent].accumulations
        
        #Use ML_mesa MetaAgent Buffer otherwise error
        #for agent in meta.agent_buffer(): 
        #store actual
        actual = agent.accumulations
        #replcae your accumulations with those of the lowest
        agent.accumulations = psuedo_accs
        #move with this new percpetion
        agent.move()
        #return you accumulations
        agent.accumulations = actual
        agent.eat()
        agent.die()
        if agent.status == "dead":
            return
        agent.trade()
            
    def step_mid(self,agent, meta):
        mid_sug = []
        mid_spice = []
        
        
        #identify the highest
        for status in meta.sub_agents.values(): 
            mid_sug.append(status.accumulations[1])
            mid_spice.append(status.accumulations[2])
        
        
        psuedo_accs = {1: gmean(mid_sug), 2: gmean(mid_spice)}
        
        #Use ML_mesa MetaAgent Buffer otherwise error
        #store actual
        actual = agent.accumulations
        #replcae your accumulations with those of the lowest
        agent.accumulations = psuedo_accs
        #move with this new perception
        agent.move()
        #return you accumulations
        agent.accumulations = actual
        agent.eat()
        agent.die()
        if agent.status == "dead":
            return
        agent.trade()
    
    
    
    
    def step(self, agent): 
        '''
        Purpose: Replace agent step function with one which follows an 
        organizational policy of all the agents
        '''
        #print (agent.model.ml.reverse_meta)
        meta = agent.model.ml.get_agent_group(agent, None)
        
        
        if self.policy_type == "low focus":
            self.step_low(agent, meta)
        elif self.policy_type == "high focus":
           self.step_high(agent, meta)
        else: 
            self.step_mid(agent, meta)
        # add relationship between meta_agents
        
        
                