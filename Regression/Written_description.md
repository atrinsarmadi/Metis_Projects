# Regression Course Project: Predict Revenue of a Successful Theatrical Movie

## Abstract

We can guess that some movies are going to be successful; Investors and producers can even guess better than us, but how successfull, let's build a model that can answer that. This model can help investors, producers and other stakeholders in predicting the revenue that a movie is going to generate in theaters at the end of the domestic opening. Predicting this value at this stage helps with carrying out business and logistics plans, as well as planning out future investments.
This project uses linear regression to find relationship between features of a movie and the target, which in our case is the original release worldwide gross. The features are mostly attributes that are known before the movie premiers, with the exception of one, which is domestic opening gross. Domestic opening is the revenue that a movie collects at the end of the first Sunday that it premiers. 
Data was scraped from [Box Office Mojo](https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW&ref_=bo_cso_ac) and manipulated using multiple Python tools.


## Design
This model is designed around studying the top 1000 movies with the highest worldwide gross and finding relationship between features of the movie and the target value, which is original release worldwide gross. The target is chosen specifically as the original release gross and not lifetime, to avoid advantages that older movies would have over newer movies, with some releasing their movies in theaters multiple times. The features chosen for this study are budget, running time, genres, domestic opening, MPAA rating and year of release. 


## Data
Data was scraped from [Box Office Mojo](https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW&ref_=bo_cso_ac) and manipulated using multiple Python tools. The scraped data included 1000 movies and 11 features, which after cleaning the data points without viable feature data, the number of data points came down to 800. After studying the data and trying out different feature engineering methods, I decided to include dummy variables for some categorical data such as genres and MPAA rating. I chose to keep the top 10 genres which had at least more than 100 movies in the database each, and summed the rest of the genres into a new feature, other genres.


## Algorithm
The scraped data was converted to pandas dataframes and multiple other tools were used to manipulate and study the data. After creating dummies, I tried other feature engineering methods such as squaring budget and year of release, and adjusting monetary values with inflation using CPI package. However, the only methods that increased model accuracy were including dummy variables, so I discontinued other feature engineering approaches. 
I evaluated multiple regression models, baseline models both for databases with and without dummy varibales. Knowing that I had large number of features compared to my data points, and the features had very different units, I decided to standardize coefficients using Scikit learn scaler method. RidgeCV and LassoCV had very similar results on the standardized data, but I decided to use LassoCV as my final model, since it was preferable to reduce number of features, which LassoCV was successful in removing 3 types of genres.


## Tools
- Web Scraping using BeautifulSoup and Requests in Python
- Pandas, Numpy, Matplotlib, Seaborn Python packages for manipulating data and showing results
- Scikit learn and statsmodel packages for running regression models

## Communication
Here[https://github.com/atrinsarmadi/Metis_Projects/tree/main/Regression] is the slides and visulas presented at the end of the project.
