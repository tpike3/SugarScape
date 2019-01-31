# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:53:09 2018

@author: ymamo
"""

from NetScape import NetScape
import visualization
import time
import recorder
import pickle


'''
visualization.server.launch()
'''
'''
test = NetScape(height = 50, width = 50, initial_population =200, regrow = 1, Moore = False)
#print (test.schedule.get_breed_count(A.SugarAgent))

for s in range(1000):
    test.step()
   

print (test.ml.active_agent_count)
print (test.ml.agent_count)
price_record = test.price_record

#pickle.dump(price_record, open( "price_record.p", "wb" ))
#pickle.dump(test.datacollector.get_table_dataframe("Health"), open("Agent_stats.p", "wb"))
#pickle.dump(test.datacollector.get_table_dataframe("Time"), open("Time_stats.p", "wb"))


'''
survivors = []
time2 = []
price_df = {}



for run in range(100):
    print ("RUN: ", run)
    test = NetScape(height = 50, width = 50, initial_population = 200, regrow = 1, seed = 42)
    
    for s in range(1000):
        test.step()
    df = test.datacollector.get_table_dataframe("Time")   
    price_df["Run"+str(run)] = test.price_record
    agents = test.ml.agent_count
    survivors.append(agents[1][1])
    time2.append(df["Time Per Step"].sum())
    
pickle.dump(price_df, open("net_total_price.p", "wb"))
pickle.dump(survivors, open("net_multi_sur.p", "wb" ))
pickle.dump(time2, open("net_multi_time.p", "wb"))
