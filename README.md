# Movie_Income_Prediction
The movie industry is huge income generater in the entertainment industry, there are many variables that contributes to how successful a movie is, but it's hard to understand how these variables work. 

![Image of movie trends by time and lable](https://www.cdc.gov/pcd/issues/2012/images/12_0170_03.gif)
![Image of movie income] (http://www.thesoobproductions.co.uk/wp-content/uploads/2012/10/movie-money-film-reel.ju_.09.jpg)

This project aims to **predict movie profit (revenue - budgeted cost)** based on genre, director(s), actor(s)/actress(es), release season (month), rating (R, PG13...), other movies released in the same time and popularity (number of votes). 

There are two datasets for this project. The first is the basic details regarding movies, including genre, directors, actors, lables, release, rating, and popularity. This data will be coming from an API call to IMDB. The second set of data looks at profit information regarding a movie. The two datasets will be linked through **imdb id** which is available on both datasets as unique identifier.

API Data accessed:
IMBD movie informaiton
http://www.imdb.com/interfaces/

Movie DB profit information
https://developers.themoviedb.org/3/movies/get-movie-details

Collaborators:
Anna Huang, Jingyun Chen, Weichen Xu, Chen Ren, Junmeng Zhu
