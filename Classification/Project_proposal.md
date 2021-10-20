# Project Proposal - SF Bay Area Bike Share Growth Plan

## Question
Kickstarter is a website that helps in bringing creative projects to life. They achieve this mission by offering project ideas to their users and democratizing funding process. Anyone can share their project idea or product description on their website, which allows the viewers to fund the projects they like and hence participate in deciding if the campaign would be successful. For this project I'd like to look at recent historical data from Kickstarter projects in 2021, scraped by Web Robots at [link](https://webrobots.io/kickstarter-datasets/), and train and evaluate classification models that can predict if a campaign would be successful or failed. 
This model can be used by Kickstarter or entrepreneurs:
1. Kickstarter can use this model to predict which campaigns are more likely to succeed, and use the prediction to increase advertising for successful projects, by grouping with other campaing categories, right placement of ads or link connections on their website.
2. This model can also be provided as a paid service to entrepreneurs who are starting a campaign on Kickstarter website. The model can share predictions about the campaign success, and in the case of failure, allow the entrepreneurs to adjust their campaign features in order to increase their chance of success. In the future this step can be automated in order to suggest adjustments to project requirements to any entrepreneur using the service in order to increase the likelihood of campaign success.

## Data Description
The data will be downloaded/scraped from [Web Robots](https://webrobots.io/kickstarter-datasets/) which scrapes all kickstarter projects almost every month. I plan to use at least 10000 valid data points from 2021. The raw data has 39 features, which some of the most important are funding goal, number of backers, category, when the project was created, deadline for funding, pledged and lastly if successful or failed, which means if the pledged value was able to meet the funding goals.

## Algorithms
I will use multiple classification models to evaluate the best model to be used for this prediction. I will perform some techniques to prepare data for classification models such as feature engineering, regularization, etc.

## Tools
I plan to use sql to perform some of the data cleaning and store the database. I will use Python classification packages to build classification models, and Python visualization packages for data visualization. 

## MVP Goal
