def get_tmdb_id_list(start_year, end_year, start_page, end_page):
    """function to get all Tmdb_id"""

    import requests

    TMDB_KEY = '60027f35df522f00e57a79b9d3568423'
    year = range(start_year, end_year)
    page_num = range(start_page, end_page)
    id_list = []

    tmdb_id_query = "https://api.themoviedb.org/3/discover/movie?" \
                    +"api_key=%s" \
                    +"&language=en-US&sort_by=release_date.asc" \
                    +"&sort_by=popularity.desc" \
                    +"&include_adult=false&include_video=false" \
                    +"&page=%d" \
                    +"&primary_release_year=%d"

    for n in page_num:
        for yr in year:
            rq = requests.get(tmdb_id_query % (TMDB_KEY, n, yr)).json()
            for item in rq['results']:
                id_list.append(item['id'])

    return id_list

def get_profit(start_year, end_year, start_page, end_page):
    """call procedure to get profit data of a particular movie (id)"""

    import requests
    import json
    import pandas as pd

    TMDB_KEY = '60027f35df522f00e57a79b9d3568423'
    TMDB_ID_LIST = get_tmdb_id_list(start_year, end_year, start_page, end_page)
    query = "https://api.themoviedb.org/3/movie/%d?" \
        +"api_key=%s" \
        +"&language=en-US"

    profit_dict_list = []
    for tmdb_id in TMDB_ID_LIST:
        print("getting info on IMDB ID ", tmdb_id)
        request = requests.get(query %(tmdb_id, TMDB_KEY)).json()
        profit_dict_list.append({'imdb_id':request['imdb_id'],
                                 'revenue': request['revenue'],
                                 'budget': request['budget']})

    profit_df = pd.DataFrame(profit_dict_list)
    return profit_df


def get_info(start_year, end_year, start_page, end_page):
    """based on imdb ids get relevant movie info"""

    import requests
    import json
    import pandas as pd
    from datetime import datetime
    OMDB_KEY = "4c427520"


    #get imdb_id_list from csv
    profit_df = get_profit(start_year, end_year, start_page, end_page)
    # print profit_df.head()
    imdb_id_list = profit_df['imdb_id']
    #loop through imdb_id_list to get all the rest of the variables
    dict_list = []
    for imdb_id in imdb_id_list:
        query = ' http://www.omdbapi.com/?i=%s&apikey=%s'
        r = requests.head(query % (imdb_id, OMDB_KEY))
        #print r.status_code
        if r.status_code == 200:
            try:
                rq = requests.get(query % (imdb_id, OMDB_KEY)).json()
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
    return info_df

def get_data(start_year, end_year, start_page, end_page):
    """combine two data source files"""

    start_year = int(start_year)
    end_year = int(end_year)
    start_page = int(start_page)
    end_page = int(end_page)

    print("start getting profit")
    revenue_df = get_profit(start_year, end_year, start_page, end_page)
    print("start getting movie info")
    info_df = get_info(start_year, end_year, start_page, end_page)
    print("start comibing data")
    combine_df = revenue_df.join(info_df, lsuffix='imdb_id', rsuffix='imdbID')
    print("data_crawling finished!")

    return combine_df
