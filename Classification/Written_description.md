# Kickstarter Campaings - Predicting Failed Projects

## Abstract
Kickstarter is a website that allows people to upload project ideas, and anyone can fund/invest in the idea. Kickstarter gathers its revenue from 5% of the funds pledged to successful projects. Increasing the percentage of successful projects in Kickstarter leads to increase in revenue. Campaigners also do not have a tool to identify or judge how well their project is going to perform. Being able to study what makes a successful vs failing project is helpful in relying this information from historical data and scientific statistical evaluations to the enterpreneurs so that they can increase their chance of success. On average, it takes campaigners 60 days to prepare campaign page and launch the project. Average campaign runs for 32 days. Being able to evaluate your project further is helpful in moving you almost 3 months in advance.
The goal of this project is to look at historical data from Kickstarter projects, scraped by Web Robots at [link](https://webrobots.io/kickstarter-datasets/), and train and evaluate classification models that can predict if a campaign would most likely succeed or fail. This model can be used by Kickstarter as a paid or free service to entrepreneurs in order to evaluate likeliness of success/failure of their projects. Increasing project success is in Kickstarter's interest as their revenue is taken from 5% of the successfully funded projects.


## Data
The data is gathered from [link](https://webrobots.io/kickstarter-datasets/). I downloaded all the scraping files from 2021 which included projects from 2015 to present. It is unknown if this dataset contains all the projects during this timeframe, but since we are interested in classification of the outcome of the project and not a descriptive comparison, this uknown should not be an issue. Dataset initially contained 1.2m projects and 39 attributes. After EDA and feature engineering, the data was reduced to ~31k projects and 9 main attributes (numerical and categorical).
All the CSV scraped files were read and all the data were input in a large dataset. The attributes were reduced to those that are known before a campaign launches. Only projects that had status of successful or failed were kept, so cancelled or live projects were eliminated. Time variables were in seconds so they were all converted to datetime objects and used for retrieving campaign and preparation durations.


## Design
The target is chosen as the failed projects because it is most important to identify which projects are likely to fail and adjust the features for those projects. The distribution of successful to failed projects are almost 76% to 24%, so it also helps to choose the lower proportional variable like failed project here as the target. The impact of this identification and adjustment is increasing kickstarter project success which leads to increase of revenue, as well as avoiding almost ~average 3 months of preparation and campaign run per project. 


## Algorithm
There are multiple classification models that one can train and evaluate data on. The common approach is to evaluate which method is the best performing among all, using metrics such as F1 and ROC-AUC curve. The evaluations were done at the same time of initial hyperparameter tuning for each model. XGBoost was chosen as the top performer using ROC-AUC curve metric, also having highest F1 score along with Random Forest. 



## Tools
- Python Pandas and Numpy for data exploration
- Scikit Learn for Classification Modeling and evaluation
- Matplotlib and Seaborn for Data visualization

## Communication
[Here](https://github.com/atrinsarmadi/Metis_Projects/tree/main/Classification) is the slides and visulas presented at the end of the project.
