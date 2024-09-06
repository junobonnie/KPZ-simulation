# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:13:27 2024

@author: replica
"""
import matplotlib.pyplot as plt
import random as r
import numpy as np

def init(map_):
    for i in range(width):
        map_[0][i] = 2

def random_generator(map_, prob):
    for i in range(width):
        if r.random() < prob:
            map_[height-1][i] = 1

def update(map_):
    for i in range(width):
        for j in range(height):
            if map_[j][i] == 1:
                map_[j][i] = 0
                map_[j-1][i] = 1
                
                if i+1 == width:
                    if map_[j-2][i] == 2  or map_[j-1][i-1] == 2:
                        map_[j-1][i] = 2
                elif i-1 == -1:
                    if map_[j-2][i] == 2 or map_[j-1][i+1] == 2:
                        map_[j-1][i] = 2
                else:
                    if map_[j-2][i] == 2 or map_[j-1][i+1] == 2 or map_[j-1][i-1] == 2:
                        map_[j-1][i] = 2
                        
def get_heights(map_, heights):
    for i in range(width):
        for j in reversed(range(heights[i], height)):
            if map_[j][i] == 2:
                heights[i] = j
                break
    return heights

def height_std_l(heights, length):
    height_std = 0
    num = width-length+1
    for i in range(num):
        height_std += np.std(heights[i:i+length])
    height_std /= num
    return height_std
    
height, width = 1000, 500
time = np.arange(4501)
set_time = [1010, 1100, 2000, 3000, 4000, 4500]
L = np.arange(1, 100)

map_ = [[0 for i in range(width)] for j in range(height)]
heights = [0 for i in range(width)]

init(map_)
W = []
for t in time:
    random_generator(map_, 0.1)
    update(map_)
    heights = get_heights(map_, heights)
    W.append(np.std(heights))
    if t in set_time:
        Wl = []
        for l in L:
            Wl.append(height_std_l(heights, l))
        plt.figure(dpi=300)
        plt.title("time = %d"%t)
        plt.imshow(map_)
        plt.gca().invert_yaxis()
        plt.axis('off')
        plt.show()
        
        kpz = (4/5)*L**(1/2)
        plt.figure(dpi=300)
        plt.title("time = %d"%t)
        plt.plot(L, Wl, label="KPZ Simulation")
        plt.plot(L, kpz, label="Family–Vicsek scaling relation")
        plt.legend()
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel("length")
        plt.ylabel("Standard Deviation of Heights")
        plt.show()
    #plt.figure(dpi=300)
    #plt.imshow(map_)
    #plt.gca().invert_yaxis()
    #plt.axis('off')
    ## plt.show()
    #plt.savefig("images/%08d.png"%(t), bbox_inches='tight', pad_inches = 0)
    #plt.close()
    print(t)


kpz = (4/5)*(width**0.5) * ((time-height+3)/width**1.5)**(1/3)
plt.figure(dpi=300)
plt.plot(time, W, label="KPZ Simulation")
plt.plot(time, kpz, label="Family–Vicsek scaling relation")
plt.legend()
plt.xlabel("time")
plt.ylabel("Standard Deviation of Heights")
plt.show()


    
