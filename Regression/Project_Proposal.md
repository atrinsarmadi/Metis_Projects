# Project Proposal

## Question
The goal of this project is to predict profitability of a movie based on multiple features such as budget, release date, genre, distributor, ratings, 1st weekend and 1st week box office gross. The model for this analysis is a linear regression model that will predict Total Gross values based on the features described.
This analysis helps producers and movie studios to make decisions on what movies to make to reach profitability goals and how to budget their movie productions depending on the type of movie.  

## Data Description
The data will be scraped from [Box Office Mojo](https://www.boxofficemojo.com), [IMDB](https://www.imdb.com), and [Rotten Tomatoes](https://www.rottentomatoes.com). The bulk of the data will be centered around features described in the question, as well as targets such as total gross or total gross over budget ratio in order to train and evaluate models. The focus of the data will be around movies released in the 21st century. 


## Tools
To perform webscraping, Beautiful Soup package will be used with python to scrape and parse HTML data, Selenium will be used if browser automation is required in the webscraping process. To clean and manipulate data, python and packages such as numpy and pandas will be used, and visualization will be performed with python matplotlib and seaborn packages.


## MVP Goal
The MVP of this project is to perform webscraping on relevant data for features and targets from some of the websites listed. The MVP also includes linear regression models to predict Total Gross values of movies based on features of a movie, leading to conclusions for decision making in movie investments. 

