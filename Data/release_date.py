import pandas as pd
import datetime

def Update_released_date(filename):
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
    data.to_csv("FinalMerge_updateson_releaseddate.csv")



if __name__ == "__main__":
    Filename = "FinalMerge.csv"
    Update_released_date(Filename)