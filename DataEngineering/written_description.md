# SF Parking Meter Recommendation System

## Abstract
Parking regulations are confusing. Often we drive to a destination such as a workout class or a dentist appointment and we find ourselves driving around trying to find a parking spot that fits the parking schedule that we are looking for, sometimes even after parking and going to the parking meter we realize the limit is not sufficient, or when we are walking back from the appointment, we realize the parking spots a couple of blocks away were a couple of dollars cheaper per hour. With a help of a recommender system, you can check parking meter and regulations ahead of time, choose one based on distance, price and time limit, and input the meter address instead of your destination.

For this project I use two parking meter datasets provided by city of San Francisco, and available through Sodapy API. First dataset is the list of all parking meters in the city, with relevant information such as location coordinates. Second dataset is the parking meter regulations based on day and time. Parking meters have different hourly prices and time limits on different days and times of the day. I created a web app interface using Streamlit where client can input variables such as the destination address, maximum distance they are willing to walk, the start and end time of their parking and day of week. Using this information, I filter relevant parking meters and recommend top spots based on cost and distance.


## DATA
The datasets are downloaded from [SF city open data website](https://data.sfgov.org/Transportation/Parking-Meters/8vzz-qzz9) and [here](https://data.sfgov.org/Transportation/Meter-Policies/qq7v-hds4). The first dataset is the list of the parking meters, including about 34k rows, each representing a parking meter. I use parking space IDs and the location coordinates in this dataset. The second one includes the meter policies based on day of week and time of day, updated weekly. It includes around 1m rows each representing a parking meter policy on a certain day and time interval. I use second dataset to filter relevant variables and calculate total cost of parking. 


## Design
The data is downloaded using the Sodapy API and stored in a SQLite database. It is then imported to Pandas for processing where parking meters are filtered based on client inputs, destination is converted to coordinates using Google Maps API Geocoding. The cost of parking is calculated on filtered parking meters, and the top parking meters are sorted based on cost and then distance. The parking meters are represented in two method, on a map, as well as a list presenting the distance, cost and address of the parking meter.


## Algorithm



## Tools
- Sodapy API for data acquisiton
- Python Pandas and Numpy for data exploration and processing
- Schedule for weekly update of the database
- SQLite and SQLAlchemy for data storage
- Requests and Geopy using Google Maps API for Geocoding and Reverse Geocoding
- Streamlit for web app creation, visulization and interface

## Communication
[Here](https://github.com/atrinsarmadi/Metis_Projects/tree/main/DataEngineering) are the slides and visulas presented at the end of the project.
