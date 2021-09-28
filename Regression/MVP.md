# Linear Regression model of top 1000 gross movies
The goal of this project is to build a linear regression model of the top 1000 movies with the highest world lifetime gross. This model would ideally be used as a prediction tool for investors and producers in order to predict the original release worldwide gross value based on features such as budget, rating, running time, domestic distributor, domestic opening gross, MPAA rating, and genres.

## DATA Gathering
The data is scraped from [Box Office Mojo](https://www.boxofficemojo.com), specifically [Top Lifetime Worldwide Gross Table](https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW) that has listed top 1000 movies in this category. I used BeautifulSoup and Requests to perform webscraping and parsing HTML data, which led to gathering a dataframe with 990 movies and 17 attributes. After performing some exploratory data analysis and cleaning the data, I decided to keep 8 Attributes of each movie, 7 of them are features as listed above and the target of this model is Original Release Worldwide Gross. The reason that this target was chosen over worldwide lifetime gross value is that some movies had multiple releases over time, and this would create an advantage for movies that are older and had multiple releases. I will also look further into standardizing the original release worldwide gross value by considering inflation rates over the years since the release of each movie.
I have also removed movies that were missing budget values, bringing the total number of movies as our data points to 800. Out of this 800 movies, 13 are missing running time values which I will replace with the mean of running time values from the rest of the movies. 

Here is how the dataframe looks at this stage:
![DataFrame](https://user-images.githubusercontent.com/47256224/135166959-af6d0a35-4d66-4ebc-8310-16151e9c895e.png)

## Initial Findings
The project is currently in the middle of the EDA stage. Without looking at the complete dataframe, as it is still required to create dummy variables from categorical data and continue cleaning the data, we can look at the pairplots of the numerical values, in order to graps an initial understanding of the data distribution.

![pairplot](https://user-images.githubusercontent.com/47256224/135168116-224633f0-d88c-42f4-b497-fe29cc5f2de2.png)

From the pairplot we can see that apart from creating dummy variables, most probably some more cleaning, standardizing and regularization of the data is required on variables such as budget and running time.


## Future work
The future work of this project is categorized in the list below
1. Complete EDA
      - Data cleaning
      - Creating dummy variables from categorical data
2. Create a baseline linear regression model
3. Refine the model
      - Most probably will include processes such as standardization and regularization
5. Finalize the model and obtain final results
6. Interpret results
