# Business Course Project: Supply and Demand Analysis of SF Bike Share

## Abstract
One of the main objectives of future urban plans is accessibility to greener transporation means. Life after pandemic has also prompted some questions about the future of personalized transportation that can increase social distancing and reduce possibilities of another pandemic. [SF Bay Area has long-range plans for 2040 and 2050](https://mtc.ca.gov/planning/long-range-planning) which includes bike share program and extension plans. For this project, I studied the [SF Bay Area Bike Share dataset from Kaggle](https://www.kaggle.com/benhamner/sf-bay-area-bike-share) to analyze the supply and demand of the bikes at each station and find opportunities in adding more bikes or open docks in some stations that fall short of either of the resources when demand is high. Bay wheels, the company who owns the bike share program can use this analysis to protrize stations that require optimization or adjustments in the number of bikes or docks they provide.


## Data
The data is gathered from [SF Bay Area Bike Share dataset from Kaggle](https://www.kaggle.com/benhamner/sf-bay-area-bike-share). It contains 4 csv files and a database for data from August 2013 - Augsut 2015. It includes station information across all Bay Area locations, status information (with number of bikes and docks available) that is taken every minute from each station, trip information with start and end stations and date and time of the trip, and weather data for those two years.


## Design
The data is very large and quite difficult to process on a personal computer. This project also requires data exploration in Spreadsheets, due to these two limitations I decided to perform an initial study on trip information from the last 3 months of data, between June and August 2015. My final goal is to study station status for a period of time that can show us a trend or instances where there is limited availability of bikes or open docks. One of the major problems I imagine Bay Wheels will have with increase of demand is to analyze and optimize accessibility to bikes and open docks whenever and wherever demand is present from customers. Before diving into status information, I decided to confirm that there is a 

**Assumptions**
- Assuming that WTWY gala is held at the end of June, data is gathered for almost 4 months between March and June.
- It is assumed that the gala is happening pre-pandemic, hence data was gathered from the year 2019.
- Based on study of turnstile throughput from turnstile manufacturers, concensus between manufacturers is that each turnstile can support a flow of 20-30 people per minute, however, to be more conservative in removing outliers from the data, a throughput of 1 person per second was chosen, leading to almost 15000 people entries per turnstile in a 4 hour period.
- Total traffic means the combination of entries and exits values for each turnstile/station.


## Algorithm
A database was created from the data using SQLite and SQLAlchemy. I continued exploring the data and converted the filtered database to Pandas dataframe using SQLAlchemy. 
Cleaning the data consisted of standardizing column names, removing duplicates, organizing the Entries and Exits data per correct entry time, and eliminating outliers by removing each turnstile entries or exits that were higher than 15000 in a 4 hour period. 
I used Pandas to continue data manipulation, grouping the turnstile features together as well as traffic data at each station. Analysis of data included:
- combining total traffic for all the stations during the 4-month period to get the highest trafficked stations
- Average commuters per day of week for top 5 stations
- Traffic per time of day for each day of the week for top 5 stations

## Tools
- SQLlite and SQLAlchemy to store and explore data
- Numpy and Pandas for data manipulation
- Matplotlib for data visualization

## Communication
[Here](https://github.com/atrinsarmadi/Metis_Projects/tree/main/EDA) is the slides and visulas presented at the end of the project.
