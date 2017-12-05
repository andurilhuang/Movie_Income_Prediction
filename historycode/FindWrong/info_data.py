def info_data():   
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


    #combine_df = profit_df.join(info_df,lsuffix='imdb_id', rsuffix='imdbID')
    #combine_df.to_csv('CombinedData_2.csv')
if __name__ == "__main__":
    info_data()
