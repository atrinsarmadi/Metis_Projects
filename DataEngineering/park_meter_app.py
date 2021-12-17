
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import requests
import time
import numpy as np
from math import radians, cos, sin, asin, sqrt
import datetime
from geopy.geocoders import GoogleV3


st.write(
'''
# Park Meter Recommendation App
''')


#Ask for inputs from user
address = st.text_input('Enter destination address:')

distance_input = st.selectbox(label='Select maximum distance:', 
	options = ['0.1', '0.25', '0.5', '1'])

time_options = (['00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00', '06:00:00',
	'07:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00', '14:00:00',
	'15:00:00', '16:00:00', '17:00:00', '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00',
	'23:00:00', '23:59:00'])
start_time_input = st.selectbox(label='Select start time:', options = time_options)
end_time_input = st.selectbox(label='Select end time:', options = time_options)
dayofweek_input = st.selectbox(label='Select day of week:', options = ['Mo','Tu','We','Th','Fr','Sa','Su'])

#Import data
park_meters = pd.read_csv('park_meter_clean.csv')
meter_policies = pd.read_csv('meter_policies_clean.csv')


#Convert destination address to destination lat & long
def get_address_query(address):
    
    address = str(address)
    address_query = address.replace(',', '').replace(' ','+') 
    API_key = 'AIzaSyDexhK1CyLC9hvi2hRUqSuzf0JGhVwUqPM'
    query = f"https://maps.googleapis.com/maps/api/geocode/json?address={address_query}&key={API_key}"
    
    response = requests.get(query)
    resp_json_payload = response.json()
    dest_lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    dest_lon = resp_json_payload['results'][0]['geometry']['location']['lng']
    return dest_lat, dest_lon

dest_lat, dest_lon = get_address_query('3514 25th St, San Francisco, CA')


#Get distance for all parking meters
def get_distance(park_meter_lat, park_meter_long, dest_lat = dest_lat,dest_lon = dest_lon):
    r = 3956
    park_meter_lat, park_meter_long, dest_lat, dest_long = (radians(park_meter_lat), 
                                                            radians(park_meter_long), radians(dest_lat), 
                                                            radians(dest_lon)) 
    dlat = dest_lat - park_meter_lat
    dlong = dest_long - park_meter_long
    a = sin(dlat / 2)**2 + cos(park_meter_lat) * cos(dest_lat) * sin(dlong / 2)**2
    c = 2 * asin(sqrt(a))
    dist = c * r
    return dist

park_meters['dist'] = park_meters.apply(lambda row: 
                                    get_distance(row['latitude'], row['longitude'], dest_lat , dest_lon), 
                                    axis = 1)


#Filter meter list & policies based on distance, day of week and time
park_meters = park_meters[park_meters['dist'] < float(distance_input)]

filtered_meter_policies = meter_policies[meter_policies['parkingspaceid'].isin(
	park_meters['parking_space_id'])]

filtered_meter_policies = filtered_meter_policies[filtered_meter_policies['dayofweek'] == dayofweek_input]

filtered_meter_policies = filtered_meter_policies[(((filtered_meter_policies['starttime'] <= start_time_input) & 
                          (start_time_input < filtered_meter_policies['endtime'])) |
                         ((filtered_meter_policies['starttime'] < end_time_input) & 
                          (end_time_input <= filtered_meter_policies['endtime'])))]

# Filter dataframe based on time limit
spaces_to_remove = set()
def check_time_limits(row, start_time, end_time):
    phase_start = pd.to_datetime(row['starttime'])
    phase_end = pd.to_datetime(row['endtime'])
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)
    #Scenario 0 : no time limit
    if row['timelimitminutes'] == 0.0:
        pass
    #Scenario 1: All of trip in one phase
    elif (phase_start <= start_time) & (phase_end >= end_time):
        if (end_time - start_time)/datetime.timedelta(minutes=1) > row['timelimitminutes']:
            spaces_to_remove.add(row['parkingspaceid'])
    #Scenario 2: Trip starts in that phase but goes beyond
    elif (phase_start <= start_time) & (phase_end < end_time):
        if (phase_end - start_time)/datetime.timedelta(minutes=1) > row['timelimitminutes']:
            spaces_to_remove.add(row['parkingspaceid'])
    #Scenario 3: Trip started before this phase but ending in this phase
    elif (phase_start > start_time) & (phase_end >= end_time):
        if (end_time - phase_start)/datetime.timedelta(minutes=1) > row['timelimitminutes']:
            spaces_to_remove.add(row['parkingspaceid'])
    #Scenario 4: This phase is in the middle of the parking schedule
    elif (phase_start >= start_time) & (phase_end <= end_time):
        if (phase_end - phase_start)/datetime.timedelta(minutes=1) > row['timelimitminutes']:
            spaces_to_remove.add(row['parkingspaceid'])
    else:
        pass
    return spaces_to_remove

filtered_meter_policies.apply(check_time_limits,start_time=start_time_input, end_time=end_time_input, axis=1)

filtered_meter_policies = filtered_meter_policies[filtered_meter_policies['parkingspaceid'].isin(spaces_to_remove) == False]

#Get cost per line
def get_cost(row, start_time, end_time):
    #Get cost per line
    
    phase_start = pd.to_datetime(row['starttime'])
    phase_end = pd.to_datetime(row['endtime'])
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)
    #Scenario 0 : no hourly cost
    if row['hourlyrate'] == 0.0:
        row['cost'] = 0
    #Scenario 1: All of trip in one phase
    elif (phase_start <= start_time) & (phase_end >= end_time):
        row['cost'] = (end_time - start_time)/datetime.timedelta(hours=1) * row['hourlyrate']
    #Scenario 2: Trip starts in that phase but goes beyond
    elif (phase_start <= start_time) & (phase_end < end_time):
        row['cost'] = (phase_end - start_time)/datetime.timedelta(hours=1) * row['hourlyrate']
    #Scenario 3: Trip started before this phase but ending in this phase
    elif (phase_start > start_time) & (phase_end >= end_time):
        row['cost'] = (end_time - phase_start)/datetime.timedelta(hours=1) * row['hourlyrate']
    #Scenario 4: This phase is in the middle of the parking schedule
    elif (phase_start >= start_time) & (phase_end <= end_time):
        row['cost'] = (phase_end - phase_start)/datetime.timedelta(minutes=1) * row['hourlyrate']
    else:
        pass
    return row

filtered_meter_policies = filtered_meter_policies.apply(get_cost,
	start_time=start_time_input, end_time=end_time_input, axis=1)

grouped_cost = filtered_meter_policies.groupby(['parkingspaceid']).sum(['cost'])

#Get total cost
def get_total_cost(row):
    if row['parking_space_id'] in grouped_cost.index:
        row['total_cost'] = grouped_cost.loc[row['parking_space_id']]['cost']    
    return row

park_meters = park_meters.apply(get_total_cost,axis=1)
park_meters.dropna(subset=['total_cost'], inplace=True)
park_meters.sort_values(by=['total_cost','dist'],inplace=True)

top10 = park_meters.head(10)

#Get addresses for top10
def get_address(row):
    API_key = 'AIzaSyDexhK1CyLC9hvi2hRUqSuzf0JGhVwUqPM'
    geolocator = GoogleV3(api_key=API_key)
    t = row['latitude'], row['longitude']
    row['address'] = str(geolocator.reverse(t))
    return row

top10 = top10.apply(get_address, axis=1)

#Map the parking meters
st.map(data=top10)
st.table(data=top10)


