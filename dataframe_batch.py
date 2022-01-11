# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 18:18:08 2021

@author: ankit
"""

def batchdf(df=None,chunksize=None):
      #chunk row size
    batch_df = [df[k:k+chunksize] for k in range(0,df.shape[0],chunksize)]
    
batchdf(df=df,chunksize=100) #let say that split the dataframe with row size 100