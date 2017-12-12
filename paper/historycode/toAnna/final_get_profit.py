import os
#os.chdir("C:\\Users\\Anna Huang\\Desktop\\cse583\\Movie_Income_Prediction")
import requests
import json
import pandas as pd
from datetime import datetime

TMDB_KEY = "60027f35df522f00e57a79b9d3568423"
OMDB_KEY = "d3941272"

def get_tmdb_id_list():
    """function to get all Tmdb_id between 06-16"""

    import requests
    import json
    year = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016] 
    page_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
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
        profit_dict_list.append({'imdb_id':request['imdb_id'], 'profit': request['revenue'],'budget': request['budget']})
    
    profit = pd.DataFrame(profit_dict_list)
    profit_df=profit
    #profit_df = profit[profit['profit']>0]
    profit_df.to_csv('profit_by_imdb_id.csv')
    
get_profit()