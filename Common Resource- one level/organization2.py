# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 05:41:06 2019

@author: ymamo
"""

from random import randint
from scipy.stats.mstats import gmean
from itertools import combinations
#from ML_Mesa import MetaAgent

class rules(): 
    
    def __init__(self): 
        self.metabolism = None
        #Data set up = {1 : Sugar Value, 2 : Spice Value}
        self.accumulations = None
                     
    
    def calc_accumulations(self,meta):
        
        sug_amount = 0
        spice_amount = 0
        for agent in meta.sub_agents.values(): 
            if agent.type == 'agent':
                sug_amount += agent.accumulations[1.0]
                spice_amount += agent.accumulations[2.0]
            elif agent.type == 'meta':
                sug_amount += agent.policy.accumulations[1.0]
                spice_amount += agent.policy.accumulations[2.0]
            
        
        return {1.0: sug_amount, 2.0:spice_amount}
   
     
    
    def find_trader(self, agent, meta):
       '''
       Helper Function for self.trade(): 
           
       gets_agents from nearby to trade with
       '''
        
        
       traders = []
       neighbors = [i for i in agent.model.grid.get_neighborhood(agent.pos, \
                  agent.moore, radius = agent.capability['vision'])]
                
       for n in neighbors: 
           this_cell = agent.model.grid.get_cell_list_contents([n])
           for item in this_cell: 
               if str(item) == "Agent" and item not in meta.sub_agents.values():
                   traders.append(item) #for intial step  2 agents 
                                        #may be on same grid
                                        #based on random selection    
       return traders
    
        
    def group_trade(self, agent, meta):
        
        '''
        Trade Function 
        
        GrAS p. 105
        '''
        
        agent.assess_welfare()
        
        traders = self.find_trader(agent, meta)
        
        if len(traders) > 0: 
            agent.model.random.shuffle(traders) #randomize who trade with
        else: 
            return
        
        
        for partner in traders: 
            #trade_benefit = True
            #while trade_benefit:     
            # Per trade formulation, and to prevent divison by zero warning
            if agent.MRS == partner.MRS: 
                pass
        
            else: 
                #Calculate Price
                price = gmean([agent.MRS, partner.MRS])
               
                #Draft Trade
                if price > 1: 
                    spice = price
                    sugar = 1
                else:
                    sugar = 1/price
                    spice = 1
                    
                    
                    
                
                if agent.MRS > partner.MRS: 
                    conduct = agent.draft_trade(sugar, spice, partner)
                    if conduct == True: 
                        agent.accumulations[1] += sugar
                        agent.accumulations[2] -= spice
                        partner.accumulations[2] += spice
                        partner.accumulations[1] -= sugar
                        agent.model.price_record[agent.model.step_num].append(price)
                        agent.assess_welfare()
                        partner.assess_welfare()
                        agent.make_link(partner)
                        self.accumulations = agent.accumulations
                    else: 
                        pass
                        
                        
                else: 
                    conduct = partner.draft_trade(sugar, spice, agent)
                    if conduct == True:
                        agent.accumulations[1] -= sugar
                        agent.accumulations[2] += spice
                        partner.accumulations[2] -= spice
                        partner.accumulations[1] += sugar
                        agent.assess_welfare()
                        partner.assess_welfare()
                        agent.model.price_record[agent.model.step_num].append(price)
                        agent.make_link(partner)
                        self.accumulations = agent.accumulations
                    else: 
                        pass
       
    def sub_step(self, agent, meta): 
        
    
        self.accumulations = self.calc_accumulations(meta)
        #Save agents situation
        agent.accumulations = self.accumulations
        agent.move()
        agent.collect()
        self.accumulations = agent.accumulations
        agent.die()
        if agent.status == "dead":
            return
        agent.accumulations = self.accumulations
        agent.eat()
        self.accumulations = agent.accumulations
        
        self.group_trade(agent, meta)  
    
    
    
    def step(self, agent): 
        '''
        Purpose: Replace agent step function with one which follows an 
        organizational policy of all the agents
        
        Use recursion to get ensure you get down to granular agent
        '''

        meta = agent.model.ml.get_agent_group(agent, 'trades')
        
        if meta == None:
            agent.step()
        else: 
            self.sub_step(agent, meta)
            #self.sub_step2(agent, meta)
            
        