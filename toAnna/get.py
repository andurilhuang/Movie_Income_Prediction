import os
#os.chdir("C:\\Users\\Anna Huang\\Desktop\\cse583\\Movie_Income_Prediction")
import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime

TMDB_KEY = "60027f35df522f00e57a79b9d3568423"
OMDB_KEY = "6516c507"

def get_tmdb_id_list():
    """function to get all Tmdb_id between 06-16"""

    import requests
    import json
    # from year 1996-2016
    year = range(2006,2017) 
    ## 50 pages
    page_num = range(1,50)
    id_list = []
    
    tmdb_id_query = "https://api.themoviedb.org/3/discover/movie?" \
                    + "api_key=%s" \
                    + "&language=en-US&sort_by=release_date.asc" \
                    + "&include_adult=false&include_video=false" \
                    + "&page=%d" \
                    + "&primary_release_year=%d" 
    for n in page_num:
        for yr in year:
            rq = requests.get(tmdb_id_query % (TMDB_KEY,n,yr)).json()
            for item in rq['results']:
                id_list.append(item['id'])
        
    return id_list

def get_profit():
    """call procedure to get profit data of a particular movie (id)"""
    TMDB_ID_LIST = get_tmdb_id_list()
    query = "https://api.themoviedb.org/3/movie/%d?" \
        +"api_key=%s" \
        +"&language=en-US"
        
    profit_dict_list = []   
    for id in TMDB_ID_LIST:    
        request = requests.get(query %(id,TMDB_KEY)).json()
        if request['revenue']>0 and request['budget']>0:    
            profit_dict_list.append({'imdb_id':request['imdb_id'], 'revenue': request['revenue'],'budget': request['budget']})
        else:
            pass
        #print profit_dict_list
        
    profit_df = pd.DataFrame(profit_dict_list)
    #profit_df = profit[profit['profit']>0]
    profit_df.to_csv('profit_by_imdb_id.csv')
    
get_profit()