# How to use modules
There are four main components that works as modules:
1. get_data
This component is for users to crawl data from the two data sources based on their defined parameters: start year, end year, start page, and end page. Years are used for the movie release range and pages are used to define how many pages of resutls the crawler should go through.

Avaialble functions:
get_tmdb_id_list(start year, end year, start page, end page):
this will return users a list of tmdb ids that the user can use in their own script.

get_profit(start year, end year, start page, end page):
this will return users a datafram df_profit with movie ids, revenue, and budget.

get_info(start year, end year, start page, end page):
this will return users a datafram df_info with movie ids and other relevant information like releases, directors, ratings, etc.

call_data(start year, end year, start page, end page):
this will return a complete dataframe ready for user to clean or further process with all information listed above. A csv is also generated and saved locally under the data directory name "data_raw_user.csv"

get_cleaned_data():
this will return a datafrme converting the development teams' own cleaned data ready for analysis and modelling.

sample:
get_tmdb_id_list(2011, 2012, 1, 2)

get_profit(2011, 2012, 1, 2)

get_info(2011, 2012, 1, 2)

call_data(2011, 2012, 1, 2)

get_cleaned_data()


2. clean_data
clean_analysis_data():
this allows user to clean the data they got using get_data, assuming they had already ran the funciton, or has a file in the folder. It does require the user to strictly use the file data_raw_user.csv in order to proceed.

3.

4.
