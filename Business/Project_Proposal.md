# Project Proposal - SF Bay Area Bike Share Growth Plan

## Question
There are a lot of innovations in city planning and transporation requirements. One of the main objectives of future urban plans is accessibility to greener transporation means. Life after pandemic has also prompted some questions about future of urban planning and the future of customized transportation that can increase social distancing and reduce possibilities of another pandemic. [SF Bay Area has long-range plans for 2040 and 2050](https://mtc.ca.gov/planning/long-range-planning) which includes bike share program plans and extension plans. For this project, I would like to study the [SF Bay Area Bike Share dataset from Kaggle](https://www.kaggle.com/benhamner/sf-bay-area-bike-share) to find growth opportunities based on demand and supply analysis per station, or find potential locations for future stations

## Data Description
The data will be scraped from [Box Office Mojo](https://www.boxofficemojo.com), [IMDB](https://www.imdb.com), and [Rotten Tomatoes](https://www.rottentomatoes.com). The bulk of the data will be centered around features described in the question, as well as targets such as total gross or total gross over budget ratio in order to train and evaluate models. The focus of the data will be around movies released in the 21st century. 


## Tools
To perform webscraping, Beautiful Soup package will be used with python to scrape and parse HTML data, Selenium will be used if browser automation is required in the webscraping process. To clean and manipulate data, python and packages such as numpy and pandas will be used, and visualization will be performed with python matplotlib and seaborn packages.


## MVP Goal
The MVP of this project is to perform webscraping on relevant data for features and targets from some of the websites listed. The MVP also includes linear regression models to predict Total Gross values of movies based on features of a movie, leading to conclusions for decision making in movie investments. 
