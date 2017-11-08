import os
import requests
import json
import pandas as pd
import numpy as np
import time
from datetime import datetime


TMDB_KEY = "60027f35df522f00e57a79b9d3568423"

"""
def get_tmdb_id_list():
    #function to get all Tmdb_id between 06-16

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


start = time.time()
ID_LIST = get_tmdb_id_list()
stop = time.time()
print(ID_LIST)
print(stop - start)
"""
query = "https://api.themoviedb.org/3/movie/%d?" \
        +"api_key=%s" \
        +"&language=en-US"
movie_id = 78
request = requests.get(query %(movie_id,TMDB_KEY)).json()
