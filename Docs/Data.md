# Discription of Data Used #


## Requirements ##
This project aims to predict movie profit (revenue - budgeted cost) based on genre, director(s), actor(s)/actress(es), release season (month), rating (R, PG13...), other movies released in the same time, average user ratings from IMBD and popularity (number of votes).and popularity (number of votes). We also plan to do a sentiment analysis on movie reviews and use the results as predictors to predict movie profit.  


## Sources ##
There are two datasets for this project. The first is the basic details regarding movies, including genre, directors, actors,, release year, rating, user average ratings and popularity. This data will be coming from an API call to IMDB. The second set of data looks at reviews and profit information regarding a movie. The two datasets will be linked through imdb id which is available on both datasets as unique identifier.

* IMBD API: http://www.imdb.com/interfaces
* Movie API: https://developers.themoviedb.org/3/movies/get-movie-details

## Evaluation ##
The columns of the table are data sets described in the "Data" section.
The rows are requirements of the data based on the questions you want to answer.

|Questions/Datasets|IMDB|Movie DB|
|---|---|---|
|Basic Movie Info|:heavy_check_mark:||
|Movie Profit Info||:heavy_check_mark:|
|Movie Profit Prediction|:heavy_check_mark:|:heavy_check_mark:|

