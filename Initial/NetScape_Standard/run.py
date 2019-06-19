# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:53:09 2018

@author: ymamo
"""

from NetScape import NetScape
import visualization
import recorder
import pickle
import time


'''
visualization.server.launch()
'''
'''
test = NetScape(height = 50, width = 50, initial_population =200, regrow = 1, Moore = False)
#print (test.schedule.get_breed_count(A.SugarAgent))
for s in range(200):
    test.step()
   

print (recorder.survivors(test))
price_record = test.price_record

#pickle.dump(price_record, open( "price_record.p", "wb" ))
#pickle.dump(test.datacollector.get_table_dataframe("Health"), open("Agent_stats.p", "wb"))
#pickle.dump(test.datacollector.get_table_dataframe("Time"), open("Time_stats.p", "wb"))
'''



survivors = []
run_time = []
price_df = {}
total_time = []



for run in range(1):
    print ("Run: " + str(run))
    start_time = time.time()
    test = NetScape(height = 50, width = 50, initial_population = 200, regrow = 1, seed = 42)
    
    for s in range(100):
        test.step()
    df = test.datacollector.get_table_dataframe("Time") 
    price_df["Run"+str(run)] = test.price_record
    agents = recorder.survivors(test)
    survivors.append(agents)
    run_time.append(df["Time Per Step"].sum())
    total_time.append(time.time() - start_time)
    
    

#pickle.dump(price_df, open("stan_total_price.p", "wb"))
#pickle.dump(survivors, open( "stan_multi_sur.p", "wb" ))
#pickle.dump(time, open("stan_multi_time.p", "wb"))
#print (survivors)
print (run_time)
print (total_time)
