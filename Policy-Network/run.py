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
    
    
df = test.datacollector.get_table_dataframe("Time") 
print (test.ml.active_agent_count)
print (test.ml.agent_count)
print (len(list(test.ml.net.edges())))
price_record = test.price_record
print ("Time: ", df["Time Per Step"].sum())

#pickle.dump(meta_type, open("meta_types_p.p", "wb"))
#pickle.dump(price_record, open( "price_record_p.p", "wb" ))
#pickle.dump(test.datacollector.get_table_dataframe("Health"), open("Agent_stats_p.p", "wb"))
#pickle.dump(test.datacollector.get_table_dataframe("Time"), open("Time_stats_p.p", "wb"))

'''


survivors = []
time2 = []
price_df = {}
type_df = {}



for run in range(100):
    print ("RUN: ", run)
    test = NetScape(height = 50, width = 50, initial_population = 200, regrow = 1, seed = 42)
    meta_type = {}
    for s in range(1000):
        test.step()
        
    
    df = test.datacollector.get_table_dataframe("Time")   
    price_df["Run"+str(run)] = test.price_record
    type_df["Run"+str(run)] = test.meta_type
    agents = test.ml.agent_count
    survivors.append(agents[1][1])
    time2.append(df["Time Per Step"].sum())
    
pickle.dump(type_df, open("type_df_10.p", "wb"))
pickle.dump(price_df, open("total_price_10.p", "wb"))
pickle.dump(survivors, open("net_multi_sur_10.p", "wb" ))
pickle.dump(time2, open("net_multi_time_10.p", "wb"))
