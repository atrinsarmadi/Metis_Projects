# Data Analysis of MTA Data Traffic for WTWY Street Team Placement Optimization

The goal of this project is to use [MTA turnstile data](http://web.mta.info/developers/turnstile.html) in order to optimize WTWY street team placement by the subway station entrances. The street team is directed to gather email addresses from people, which will be used to send out free gala tickets. The target audience is people who are passionate about WTWY goals and would contribute to the organization.

## DATA Analysis
To explore this goal, I gathered turnstile data from March to June 2019. These months were chosen since the gala is held at the beginning of the summer each year, so it offers street team 3-4 months to promote the event and gather email addresses. One assumption is that this event is held pre-pandemic, hence I chose 2019 as the year to gather data from.

## Initial Findings
The initial findings target first part of the problem which is discovering the locations and times where street teams can meet with the most number of people hence increasing the chance of gathering most email addresses. The first figure shows the cumulative traffic per station between the months of March and June in 2019.

![most_traffic_station](https://user-images.githubusercontent.com/47256224/133333640-2fc1691c-3f06-4fbd-8dc0-39c42a418428.png)

The figures below show the average of ridership per day of week during the months of March and June in 2019 at the two most popular stations in NYC. Preliminary results from these figures show that selecting weekdays as opposed to weekends for street team placements expose the team to more people.

![penn_state_average_day_of_week](https://user-images.githubusercontent.com/47256224/133333642-2ff51fec-9c9f-4962-b03e-b4ee48ccae02.png)
![grand_cent_average_day_of_week](https://user-images.githubusercontent.com/47256224/133333636-61573f95-b1ec-42c4-97ef-f91e65c3e9a1.png)



## Future work
1. More in depth study of the data will be performed to improve suggestions of team placement location and time. Study of time of the day per station will also be added to the analysis.
2. Geographical data such as zip code data will be taken into consideration in order to further optimize the suggestions based on target audience.
