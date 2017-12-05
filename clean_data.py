def get_act_pop_avg():
    """get average poplularity rating for actos by sampling"""

    import requests
    import json
    import numpy as np
    import random
    
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

def clean_director_actor():
    """add director_actor popularity rating"""
    import pandas as pd
    import requests
    import json
    import numpy as np

    ave_pop = 2.08979
    TMDB_KEY = '60027f35df522f00e57a79b9d3568423'

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
        Actor_Popularity.append(np.mean(pop_sum))
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
        Director_Popularity.append(np.mean(pop))
        dir_count = dir_count+1
        print (dir_count)

    df['director_popularity'] = Director_Popularity

    return df



def clean_data():
    import pandas as pd
    df = clean_director_actor()

    """preparing data for analysis"""
    
    # index of released date col
    index = df.columns.get_loc("Released")
    
    #change date data to timestamp
    date_list = pd.to_datetime(df["Released"])

    # released date is weekend or not
    weekend_list = []
    for each in date_list:
        day_ofweek = each.dayofweek
        if day_ofweek >= 4 and day_ofweek <= 6:
            tag = 1
        else:
            tag = 0
        weekend_list.append(tag)

    # released date is on dump months or not
    dumpmonth_list = []
    for each in date_list:
        month = each.month
        if month == 1 or month == 2 or month == 8 or month ==9:
            tag = 1
        else:
            tag = 0
        dumpmonth_list.append(tag)
           
    df.insert(loc=index+1,column = "Released on weekend",value=weekend_list)
    df.insert(loc=index+2,column = "Released on dump month",value=dumpmonth_list)
    #Count the number of Language
    df['Language'] = df.Language.str.count(',')+1

    #Categorize the country
    df["Country"] = df["Country"].map(lambda x: x.split(",")[0])

    #Clean IMDB.Votes
    df['IMDB.Votes'] = df['IMDB.Votes'].replace(',', '',regex=True)
    df['IMDB.Votes'] = df['IMDB.Votes'].astype(int)
    
    #Clean Runtime
    df['Runtime'] = df['Runtime'].replace('min', '',regex=True)
    df['Runime'] = df['Runtime'].astype(int)
    
    #clean column whitespace
    df['Production'] = df['Production'].str.split(' ').str.get(0)
    df = pd.concat([df, df['Genre'].str.get_dummies(sep=', ')], axis=1) 
    
    #reorganize genre grouping
    df['Thriller'] = df[['Thriller', 'Horror']].sum(axis=1)
    df['Fantasy'] = df[['Fantasy', 'Sci-Fi']].sum(axis=1)
    df['Other'] = df[['Music', 'History', 'Sport', 'War', 'Western', 'Musical', 'Documentary', 'News', 'Short']].sum(axis=1)
    df.drop(['Music', 'History', 'Sport', 'War', 'Western', 'Musical', 'Documentary', 'News', 'Short', 'Horror', 'Sci-Fi'], axis=1, inplace=True)
    
    variables = list(df)[19:32]
    for x in variables:
        df.loc[df['%s' % x] > 1, '%s' % x] = 1

    df.to_csv("data_for_lr.csv")    

if __name__ == "__main__":
    clean_data()