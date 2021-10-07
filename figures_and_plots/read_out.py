#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:11:43 2021

@author: emmadevin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob


path = glob.glob('/Users/emmadevin/Work/USGS 2021/Data/Prelim/Andrews_inversion_constrained/*.out')

for i in range(len(path)):
    data = np.genfromtxt(path[i], dtype = float, comments = '#', delimiter = None, usecols = (0,1,2)) #only read in first two cols

    freq = data.T[0]
    spectra = data.T[1]
    
    fig = plt.figure(figsize = (8,6))
    plt.style.use('classic')
    fig.patch.set_facecolor('white')
    plt.plot(freq, spectra)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('frequency (Hz)')
    plt.ylabel('amplitude')
    