# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 06:22:13 2016

@author: chihebdaoues
"""

import pylab as plt;
sample =[]
linear = []
quadratic = []
for i in range(30):
    sample.append(i);
    linear.append(2**i);
    quadratic.append(i**2);
plt.figure("lin");
plt.clf();
plt.xlabel("zooz");
plt.ylim(0,100);
plt.plot(sample,linear,label="z");
plt.legend();
plt.figure("quad");
plt.plot(sample,quadratic);