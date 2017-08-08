# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 12:24:43 2017

@author: haohong
"""
import numpy as np
#y0,y1,y2,y3,y4,y5,y6,y7=np.loadtxt("20160708_1.tsv",\
#                                   delimiter='\t',unpack=True)

import codecs
data = codecs.open("20160708.tsv", encoding='GB2312')
datalines = data.readlines()
i=0


    