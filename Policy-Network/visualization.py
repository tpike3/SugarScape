# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 06:18:02 2018

@author: ymamo
"""

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

import ResourceScape as R
import NetAgent as N
import NetScape

color_dic_sug = {4: "#005C00",
             3: "#008300",
             2: "#00AA00",
             1: "#00F800"}
             
color_dic_spice = { 4: "#D4AC0D", 
                    3: "#F1C40F",
                    2: "#F4D03F",
                    1: "#F7DC6F"}


def Agent_portrayal(agent):
    if agent is None:
        print ("no agent")
        return

    portrayal = {}

    if type(agent) is N.NetAgent:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "#2E86C1"
        portrayal["r"] = 0.7
        portrayal["Filled"] = "true"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    elif type(agent) is R.resource and \
         agent.value_sug >= agent.value_spice:
        
        if agent.value_sug != 0:
            portrayal["Color"] = color_dic_sug[agent.value_sug]
        else:
            portrayal["Color"] = "#D6F5D6"
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1
        
    else: 
        portrayal["Color"] = color_dic_spice[agent.value_spice]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1
    return portrayal


canvas_element = CanvasGrid(Agent_portrayal, 50, 50, 500, 500)
chart_element = ChartModule([{"Label": "SugarAgent", "Color": "#AA0000"}])

server = ModularServer(NetScape.NetScape, [canvas_element, chart_element],
                       "Sugarscape")