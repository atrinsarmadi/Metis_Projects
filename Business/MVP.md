## SF bike share supply and demand analysis
The objective of this project is to look at the supply and demand trends of the SF Bikeshare Stations in order to find incentives in adding bikes or docks to current stations or suggest new locations for stations.

### Data Description
The data is downloaded from [Kaggle](https://www.kaggle.com/benhamner/sf-bay-area-bike-share), and it includes station location and installation information, status of bikes in each station, trip information between stations and weather data. The data spans between August 2013 and August 2015 which is the first two years of this program. 

### Initial Findings
For first steps of analyzing this data, I merged station information with trip data in order to isolate the stations and trips that were in the city of San Francisco, removing other cities in the Bay Area. Looking at the total trip data from 2 years we can recognize a few details, the graph on the right shows that number of trips that start and end at a station are almost identical. This finding helps us taking the assumptions of start station as the demand for the bikes, and neglect end stations for some questions. We can also see the distribution of stations with their respective number of docks on the map. Looking at the average duration of trip per station is also another factor in realizing which stations are more profitable.

![Tableau](https://user-images.githubusercontent.com/47256224/137027577-acb262c4-76a3-45ed-b510-e1811254317e.png)

### Next steps
For next steps of the analysis, I would like to take in status data of stations for at least a 2 week period in summer of 2015 to study the patterns of supply and demand as well as number of bikes and docks available during a 2 week time period. The goal of this analysis is to understand the days of the week and time of day where the bikes are most in demand per station and identify trends that are useful for making decisions to add new bikes or docks to a station.
