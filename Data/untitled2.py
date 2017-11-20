#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:26:59 2017

@author: helloRC
"""
import pandas as pd
df = pd.read_csv("FinalMerge.csv",encoding="latin1")
df['Language'] = df.Language.str.count(',')+1
df["Country"] = df["Country"].map(lambda x: x.split(",")[0])

df['IMDB.Votes'] = df['IMDB.Votes'].replace(',', '',regex=True)
df['IMDB.Votes'] = df['IMDB.Votes'].astype(int)
df['Runtime'] = df['Runtime'].replace('min', '',regex=True)
df['Runime'] = df['Runtime'].astype(int)
print (df.head())
