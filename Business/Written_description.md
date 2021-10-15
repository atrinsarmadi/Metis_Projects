# Business Course Project: Supply and Demand Analysis of SF Bike Share

## Abstract
One of the main objectives of future urban plans is accessibility to greener transporation means. Life after pandemic has also prompted some questions about the future of personalized transportation that can increase social distancing and reduce possibilities of another pandemic. [SF Bay Area has long-range plans for 2040 and 2050](https://mtc.ca.gov/planning/long-range-planning) which includes bike share program and extension plans. For this project, I studied the [SF Bay Area Bike Share dataset from Kaggle](https://www.kaggle.com/benhamner/sf-bay-area-bike-share) to analyze the supply and demand of the bikes at each station and find opportunities in adding more bikes or open docks in some stations that fall short of either of the resources when demand is high. Bay wheels, the company who owns the bike share program can use this analysis to protrize stations that require optimization or adjustments in the number of bikes or docks they provide.


## Design
To optimize the street team placement in order to reach out to more people and gather more email addresses, I decided to study the data between March and June 2019. The results examined were stations with the highest total traffic (as a combination of entries and exits data) during this 4 month period, average of traffic of top 5 stations at each day of the week, and traffic per time of day for each day of the week at top 5 stations.

**Assumptions**
- Assuming that WTWY gala is held at the end of June, data is gathered for almost 4 months between March and June.
- It is assumed that the gala is happening pre-pandemic, hence data was gathered from the year 2019.
- Based on study of turnstile throughput from turnstile manufacturers, concensus between manufacturers is that each turnstile can support a flow of 20-30 people per minute, however, to be more conservative in removing outliers from the data, a throughput of 1 person per second was chosen, leading to almost 15000 people entries per turnstile in a 4 hour period.
- Total traffic means the combination of entries and exits values for each turnstile/station.


## Data
The data is gathered from the public [MTA turnstile data](http://web.mta.info/developers/turnstile.html). Based on the assumptions at the design stage, the data is gathered between March and June 2019. 

The dataset contains 3506035 rows of data showing entries and exits per turnstile at each station per 4 hour periods. 
The features for each turnstile are *C/A =  Control Area, Unit = Remote Unit for station, SCP = Subunit Channel Position representing an specific address for the device, DESC = ‘REGULAR’ scheduled audit event (every 4 hours)*. Grouping these features together allows us to gather Entries and Exits data per turnstile per 4 hours. We grouped the turnstiles traffic data at each station together to study the total traffic at each station per day and time.


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
