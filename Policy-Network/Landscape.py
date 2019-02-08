# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 06:14:39 2018


@author: Tom Pike

Sugarscape Model as base for test for ANT and MAP
Original Rob axtell and Joshua Epstein "Growing Artificial Societies: 
    Social Science from the Bottom Up"
    Washington D.C: Brookings Institute Press 1996

Adapted from Mesa 0.8.4 Jackie Kazil and David Masad

This module makes the landscape of 4 mounds for the sugar and spice world

Circle code based on Stack Overflow post by andreipmbcn at
https://stackoverflow.com/questions/21986884/
python-to-draw-a-filled-circle-on-a-grid 

"""

from itertools import chain

def inner_circle(max_r):
    '''
    Make outer circles of values to make gradient of resources
    
    Input: radius
    
    Output: List of points (tuples) in circle
    '''
        
    
    memos = []
    for k_r in range(1, max_r + 1):
        k_r_sq = k_r ** 2
        memos.append([])
        for x in range(-max_r, max_r + 1):
            x_sq = x ** 2
            for y in range(-max_r, max_r + 1):
                y_sq = y ** 2
                if x_sq + y_sq <= k_r_sq:
                    memos[k_r - 1].append((x,y))

    return list(chain.from_iterable(memos))


def outer_circle(max_r, inner, other = None, other2 = None): 
    
    '''
    Make outer circles of values to make gradient of resources
    
    input = radius, and points of other layers of circles
    
    output = list of points (tuples)  for circle portion
    '''
        
    memos = []
    outer = []
    
    for k_r in range(1, max_r + 1):
        k_r_sq = k_r ** 2
        memos.append([])
        for x in range(-max_r, max_r + 1):
            x_sq = x ** 2
            for y in range(-max_r, max_r + 1):
                y_sq = y ** 2
                if x_sq + y_sq <= k_r_sq:
                    memos[k_r - 1].append((x,y))
    
    whole = list(chain.from_iterable(memos))
    
    if other: 
        for i in other: 
            if i not in inner: 
                inner.append(i)
                
    #print (len(inner))
    if other2: 
        for i in other2: 
            if i not in inner: 
                inner.append(i) 
    #print (len(inner))
    for i in whole: 
        if i in inner: 
            pass
        else: 
            outer.append(i)
    
    return outer

def make_cirle(grad, quad): 
    
    
    if quad == 1 or quad == 3: 
        value = 4
        value2 = 0
        
        gradient = {}
        for circle in grad:
            for pos in circle: 
                gradient[pos] = (value, value2)
            value -= 1
            value2 += 1
     
        return gradient
    else: 
        value2 = 4
        value = 0
        
        gradient = {}
        for circle in grad:
            for pos in circle: 
                gradient[pos] = (value, value2)
            value2 -= 1
            value += 1
     
        return gradient


def make_quad(grad, quad, x_thrd, y_thrd, height, width): 
    
     '''
     Makes gradient of resource for each ot he 4 quadrants
     
     Provide sugar or spice attributes for each quadrant of the world    
     
     Input: points, what quadrant, a third of total world size width,
     third of world size height, height and width
     
     Output: 
         dictionary of points with resource value and type
          K = (x,y)
          V = [integer from 1 to 4, type of resource--sugar(1) and spice(2)]
     '''
     
     points = make_cirle(grad, quad)    
            
     quad_land = {}
        
     if quad == 1: 
         quad1 = x_thrd
         quad2 = y_thrd
     
     elif quad == 2: 
         quad1 = x_thrd
         quad2 = height - y_thrd
         
     elif quad == 3: 
         quad1 = width - x_thrd
         quad2 = height - y_thrd
         
     elif quad == 4: 
         quad1 = width - x_thrd
         quad2 = y_thrd
     
     for k,v in points.items(): 
        if quad == 1 or quad == 3: 
            quad_land[(k[0]+quad1, k[1]+quad2)] = v
        else: 
            #if (k[0]+quad1, k[1]+quad2) in quad_land.keys():
            #    pass
            #else: 
            quad_land[(k[0]+quad1, k[1]+quad2)] = v 
         
     
     #print (quad_land)
     return quad_land
         
         


def create_landscape(height, width):
    '''
    
    Creates a landscape with sugar and spice mounds
    
    Returns a dictionary of points which contains values 4 to 1
    and type (sugar or spice)
    
    Data Structure: 
        K = (x,y)
        V = [integer from 1 to 4, type of resource--sugar= 1 and spice = 2]
        
    '''
    
    x_thrd = int(width/2.5)
    y_thrd = int(height/2.5)
    
    #make circles
    inner = inner_circle(int(x_thrd/6))
    outer = outer_circle(int(x_thrd/3), inner)
    outer2 = outer_circle(int(x_thrd/2), inner, outer)
    outer3 = outer_circle(int(x_thrd/1.5), inner, outer, outer2)
    
    grad = [inner, outer, outer2, outer3]
    
           
    #make into 4 quadrants of square
    landscape = {}
    
    for n in [1]: 
        quad = make_quad(grad, n, x_thrd-6, y_thrd-7, height, width)
        landscape = {**landscape, **quad}
    
    for n in [2]: 
        quad = make_quad(grad, n, x_thrd-6, y_thrd-6, height, width)
        landscape = {**landscape, **quad}
    
    for n in [3]: 
        quad = make_quad(grad, n, x_thrd-6, y_thrd-6, height, width)
        landscape = {**landscape, **quad}

    for n in [4]: 
        quad = make_quad(grad, n, x_thrd-6, y_thrd -6, height, width)
        landscape = {**landscape, **quad}
    
    return landscape