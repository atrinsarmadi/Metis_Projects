# Business Course Project: Supply and Demand Analysis of SF Bike Share

## Abstract
One of the main objectives of future urban plans is accessibility to greener transporation means. Life after pandemic has also prompted some questions about the future of personalized transportation that can increase social distancing and reduce possibilities of another pandemic. [SF Bay Area has long-range plans for 2040 and 2050](https://mtc.ca.gov/planning/long-range-planning) which includes bike share program and extension plans. For this project, I studied the [SF Bay Area Bike Share dataset from Kaggle](https://www.kaggle.com/benhamner/sf-bay-area-bike-share) to analyze the supply and demand of the bikes at each station and find opportunities in adding more bikes or open docks in some stations that fall short of either of the resources when demand is high. Bay wheels, the company who owns the bikes can use this analysis to protrize stations that require optimization or adjustments in the number of bikes or docks they provide.


## Data
The data is gathered from [SF Bay Area Bike Share dataset from Kaggle](https://www.kaggle.com/benhamner/sf-bay-area-bike-share). It contains 4 csv files and a database for data from August 2013 - Augsut 2015. It includes station information across all Bay Area locations, status information (with number of bikes and docks available) that is taken every minute from each station, trip information with start and end stations and date and time of the trip, and weather data for those two years.


## Design
The data is very large and quite difficult to process on a personal computer. This project also requires data exploration in Spreadsheets, due to these two limitations I decided to perform an initial study on trip information from the last 3 months of data, between June and August 2015. My final goal is to study station status for a period of time that can show us a trend or instances where there is limited availability of bikes or open docks. One of the major problems I imagine Bay Wheels will have with increase of demand is to analyze and optimize accessibility to bikes and open docks whenever and wherever demand is present from customers. 
Before diving into status information, I decided to check a few points to confirm my later assumption to study a period of time for status information. I checked trip information for June - August 2015 and found that the number of trips taken from each station is quite similar to the number of trips ending at those stations. I also looked at the trips taken from each station for the 3 month period and observed a trend of number of trips across this time period for each station. This common trend confirms the possibility of looking at 2 weeks of data and being able to conclude results about trends or instances of low bike or dock availability.
Since status information is taken every minute at each station, the database is very large, so I decided to only look at status information for the time period between August 15 - 31, and when there is only 0 or 1 bikes available on that status, or only 0 or 1 docks are available on that status.

**Assumptions**
- Assuming that the analysis of data from 2015 can translate to a similar analysis in 2021 given we would have the data
- Based on the initial check of trip trends, I assumed that the time period of August 15 - 31 is an enough timeframe to draw some conclusions about instances of low resource availability
- I decided that low bike availablity means that there is less than 2 bikes available
- I decided that low dock availablity means that there is less than 2 docks available


## Algorithm
I started with trip CSV file and realized that my excel was too slow to process the file, so I decided to perform some initial cleaning in Pandas, removing attributes that I did not need, grab station information from station csv file, and then converted datetime variables and used in reducing the data from two years to 3 months of June to August 2015. I then converted the database to a CSV file and performed some EDA in Excel, mainly using pivot tables and graphs to study what parameters are of interest. I then uploaded the CSV file to Tableau and created some data visaulizations based on the data attributes chosen from EDA in Excel.

Status database with 72 million of rows was even too large for Pandas, so I ran a SQLite query using DB browser to grab status only for period of August 15-31, 2015, and only when there were less than 2 bikes available or less than 2 docks available. I then uploaded the new CSV file to Excel, separated bike and dock data, and performed similar operations on each sheet as follows. I separated date and time information and converted time to hourly periods. Since status is taken every 1 minute in each station, I wanted to only keep one unique value of a station during each hour, so I used a combination of if and iserror function to define one unique value from each hour and mark duplicates as errors. I then used specials to select and delete the rows with error data. I ended up with sheets only containing one count of each station for a date and hour where the resources are low. I then uploaded this Excel file to Tableau and created some visualizations as shown in the presentation.


## Tools
- SQLite and DB browser for creating custom database from one of the sheets
- Pandas for initial cleaning of one of the sheets
- Excel for EDA and data visualization
- Tableau for data visualization

## Communication
[Here](https://github.com/atrinsarmadi/Metis_Projects/tree/main/Business) is the slides and visulas presented at the end of the project.
