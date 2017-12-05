import pandas as pd
import datetime

def Cleaning_Data(filename):
    data = pd.read_csv(filename,encoding='latin1')
    # index of released date col
    index = data.columns.get_loc("Released")
    #change date data to timestamp
    date_list = pd.to_datetime(data["Released"])

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
           
    data.insert(loc=index+1,column = "Released on weekend",value=weekend_list)
    data.insert(loc=index+2,column = "Released on dump month",value=dumpmonth_list)
    #Count the number of Language
    data['Language'] = data.Language.str.count(',')+1

    #Categorize the country
    data["Country"] = data["Country"].map(lambda x: x.split(",")[0])

    #Clean IMDB.Votes
    data['IMDB.Votes'] = data['IMDB.Votes'].replace(',', '',regex=True)
    data['IMDB.Votes'] = data['IMDB.Votes'].astype(int)
    
    #Clean Runtime
    data['Runtime'] = data['Runtime'].replace('min', '',regex=True)
    data['Runime'] = data['Runtime'].astype(int)

    
    data.to_csv("FinalMerge_updateson_cleaned_data.csv")

   
    


if __name__ == "__main__":
    Filename = "FinalMerge.csv"
    Cleaning_Data(Filename)
