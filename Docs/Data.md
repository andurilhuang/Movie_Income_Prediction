# Discription of Data Used #


## Requirements ##
This project aims to predict movie profit (revenue - budgeted cost) based on genre, director(s), actor(s)/actress(es), release season (month), rating (R, PG13...), other movies released in the same time and popularity (number of votes).

## Rources ##
There are two datasets for this project. The first is the basic details regarding movies, including genre, directors, actors, lables, release, rating, and popularity. This data will be coming from an API call to IMDB. The second set of data looks at profit information regarding a movie. The two datasets will be linked through imdb id which is available on both datasets as unique identifier.

API Data accessed: IMBD movie informaiton http://www.imdb.com/interfaces/
Movie DB profit information https://developers.themoviedb.org/3/movies/get-movie-details

## Evaluation ##
The columns of the table are data sets described in the "Data" section.
The rows are requirements of the data based on the questions you want to answer.

|Questions/Datasets|IMDB|Movie DB|
|---|---|---|
|Basic Movie Info|:heavy_check_mark:||
|Movie Profit Info||:heavy_check_mark:|
|Movie Profit Prediction|:heavy_check_mark:|:heavy_check_mark:|

