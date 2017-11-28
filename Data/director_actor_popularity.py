import requests
import json
import pandas as pd
import random
import numpy as np

def get_act_pop_avg():
    
    query_ave = "https://api.themoviedb.org/3/person/popular?" \
            "api_key=60027f35df522f00e57a79b9d3568423&language=en-US&page=%d"
    
    rd = random.sample(range(1,1000),20)
    
    rd_pop=[]
    
    for n in rd:
        rq = requests.get(query_ave %n).json()
        for item in rq['results']:
            rd_pop.append(item['popularity'])
            
    ave_pop = np.mean(rd_pop)
    return ave_pop

ave_pop = 2.08979
TMDB_KEY = '60027f35df522f00e57a79b9d3568423'
import os
os.chdir("C:\\Users\\Owner\\Desktop\\583\\Movie_Income_Prediction\Data")

df = pd.read_csv("FinalMerge.csv", encoding="latin1")       

Actors_split = []
for item in df['Actors']:
    item = str(item).split(",")
    Actors_split.append(item)
    
Directors_split =[]
for item in df['Director']:
    item = str(item).split(",")
    Directors_split.append(item)

for item in Actors_split:
    for i in range(len(item)):
        item[i] = str(item[i]).strip()
        
for item in Directors_split:
    for i in range(len(item)):
        item[i] = str(item[i]).strip()        

Actor_Popularity = [] 
count = 0
url = "https://api.themoviedb.org/3/search/person"
for item in Actors_split:
    pop_sum = []
    for i in item:
        try:
            payload = {'api_key':TMDB_KEY, 'query':i, 'language':'en-US'}
            result = requests.get(url, data=payload).json()
            pop_sum.append(result['results'][0]['popularity'])
        except:
            pop_sum.append(ave_pop)
    Actor_Popularity.append(sum(pop_sum))
    count = count+1
    print(count)
df['actor_popularity'] = Actor_Popularity

Director_Popularity = [] 
dir_count = 0

for item in Directors_split:
    pop = []
    for i in item:
        try:
            payload = {'api_key':TMDB_KEY, 'query':i, 'language':'en-US'}
            result = requests.get(url, data=payload).json()
            pop.append(result['results'][0]['popularity'])
        except:
            pop.append(ave_pop)
    Director_Popularity.append(avg(pop))
    dir_count = dir_count+1
    print (dir_count)

df['director_popularity'] = Actor_Popularity

df.tail()    

        