# Linear Regression model of top 1000 gross movies
The goal of this project is to build a linear regression model of the top 1000 movies with the highest world lifetime gross. This model would ideally be used as a prediction tool for investors and producers in order to predict the original release worldwide gross value based on features such as budget, rating, running time, domestic distributor, domestic opening gross, MPAA rating, and genres.

## DATA Analysis
The data is scraped from [Box Office Mojo](https://www.boxofficemojo.com), specifically [Top Lifetime Worldwide Gross Table](https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW) that has listed top 1000 movies in this category. I used BeautifulSoup and Requests to perform webscraping and parsing HTML data, which led to gathering a dataframe with 990 movies and 17 attributes. After performing some exploratory data analysis and cleaning the data, I decided to keep 8 Attributes of each movie, 7 of them are features as listed above and the target of this model is Original Release Worldwide Gross. I have also removed movies that were missing budget values, bringing the total number of movies as our data points to 800.

## Initial Findings

## Future work
