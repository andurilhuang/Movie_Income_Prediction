def get_tmdb_id_list():
    """function to get all Tmdb_id between 96-16"""

    import requests
    import json
    year = range(1996,2016) 
    page_num = range(1,50)
    id_list = []
    
    tmdb_id_query = "https://api.themoviedb.org/3/discover/movie?" \
                    + "api_key=%s" \
                    + "&language=en-US&sort_by=release_date.asc" \
                    + "&sort_by=popularity.desc" \
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

    import requests
    import json

    TMDB_ID_LIST = get_tmdb_id_list()
    query = "https://api.themoviedb.org/3/movie/%d?" \
        +"api_key=%s" \
        +"&language=en-US"
        
    profit_dict_list = []   
    for id in TMDB_ID_LIST:
        print ("getting info on IMDB ID ",id)    
        request = requests.get(query %(id,TMDB_KEY)).json()
        profit_dict_list.append({'imdb_id':request['imdb_id'], 'revenue': request['revenue'],'budget': request['budget']})
        
    profit_df = pd.DataFrame(profit_dict_list)
    profit_df.to_csv('Revenue.csv')


def info_data():   
    """based on imdb ids get relevant movie info"""

    import os
    import requests
    import json
    import pandas as pd
    from datetime import datetime
    OMDB_KEY = "4c427520"


    #get imdb_id_list from csv
    profit_df = pd.read_csv('revenue.csv')
    # print profit_df.head()
    imdb_id_list = profit_df['imdb_id']
    #loop through imdb_id_list to get all the rest of the variables
    dict_list = []
    for imdb_id in imdb_id_list:
        query = ' http://www.omdbapi.com/?i=%s&apikey=%s'
        r = requests.head(query % (imdb_id,OMDB_KEY))
        #print r.status_code
        if r.status_code == 200:
            try:
                rq = requests.get(query % (imdb_id,OMDB_KEY)).json()
                dict_list.append({'imdbID':imdb_id,
                                'Title': rq['Title'],
                                'Country':rq['Country'],
                                'Language':rq['Language'],
                                'Released':rq['Released'],
                                'Year' : rq['Year'],
                                'Rated':rq['Rated'],
                                'Genre':rq['Genre'],
                                'Actors':rq['Actors'],
                                'Director':rq['Director'],
                                'Runtime':rq['Runtime'],
                                'IMDB Rating': rq['imdbRating'],
                                'IMDB Votes': rq['imdbVotes'],
                                'Production':rq['Production']
                                })
            except KeyError as reason:
                print(reason)
        print("Finished:"+imdb_id)
    info_df = pd.DataFrame(dict_list)
    info_df.to_csv("Info_data.csv")

def combine_data():
    """combine two data source files"""

    import pandas as pd

    print ("start getting profit")
    get_profit()
    print ("start getting movie info")
    info_data()
    print ("start comibing data")
    revenue_data = "Revenue.csv"
    info_data = "Info_data.csv"
    revenue_df = pd.read_csv(revenue_data,encoding='latin1')
    info_df = pd.read_csv(info_data,encoding='latin1')
    combine_df = revenue_df.join(info_df,lsuffix='imdb_id',rsuffix='imdbID')
    combine_df.to_csv("FinalMerge.csv")

if __name__ == "__main__":
    combine_data()    

   