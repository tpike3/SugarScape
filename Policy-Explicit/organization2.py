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
    def step_low(self, meta):
        
        lowest = None
        agent = None
        
        
        #identify the lowest
        for status in meta.sub_agents.values(): 
            if lowest == None: 
                lowest = list(status.accumulations.values())
                agent = status.unique_id
            else:
                new = list(status.accumulations.values())
                if min(lowest) > min(new):
                    lowest = new
                    agent = status.unique_id
        
        psuedo_accs = meta.sub_agents[agent].accumulations
        
        for agent in meta.agent_buffer(): 
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
                    
    def step_high(self, meta):
        
        highest = None
        agent = None
        
        #identify the highest
        for status in meta.sub_agents.values(): 
            if highest == None: 
                highest = list(status.accumulations.values())
                agent = status.unique_id
            else:
                new = list(status.accumulations.values())
                if max(highest) > max(new):
                    highest = new
                    agent = status.unique_id
        
        psuedo_accs = meta.sub_agents[agent].accumulations
        
        #Use ML_mesa MetaAgent Buffer otherwise error
        for agent in meta.agent_buffer(): 
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
            
    def step_mid(self,meta):
        mid_sug = []
        mid_spice = []
        agent = None
        
        #identify the highest
        for status in meta.sub_agents.values(): 
            mid_sug.append(status.accumulations[1])
            mid_spice.append(status.accumulations[2])
        
        
        psuedo_accs = {1: gmean(mid_sug), 2: gmean(mid_spice)}
        
        #Use ML_mesa MetaAgent Buffer otherwise error
        for agent in meta.agent_buffer(): 
            #store actual
            actual = agent.accumulations
            #replace your accumulations with those of mid
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
    
    
    
    
    def step(self, meta): 
        '''
        Purpose: Replace agent step function with one which follows an 
        organizational policy of all the agents
        '''

        if self.policy_type == "low focus":
            self.step_low(meta)
        elif self.policy_type == "high focus":
           self.step_high(meta)
        else: 
            self.step_mid(meta)
        # add relationship between meta_agents
        
        
                