# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:39:12 2021

@author: ankit
"""

import pandas as pd

df2= pd.read_csv(r"C:\ankit\exness\lead\lead_rfa_14may.csv",low_memory=False)


#n = 100000  #chunk row size
#batch_df = [df[i:i+n] for i in range(0,df.shape[0],n)]
#print("shape of df2 :",df2.shape)
def batchdf(df=None,n=None):
      #chunk row size
    batch_df = [df[k:k+n] for k in range(0,df.shape[0],n)]
    for i in range(len(batch_df)):
        #print(batch_df[i])
        batch_df[i]=batch_df[i][batch_df[i]['publisher_name'].notna()]
        batch_df[i]=batch_df[i][batch_df[i]['publisher_name']!="undefined#NA"]
        batch_df[i]=batch_df[i][['cookie_value','publisher_name','date_time','risk_remarks','client_reference_no']]
        
    df2= pd.concat(batch_df)
    return df2
     
df2=batchdf(df=df2,n=100000)
