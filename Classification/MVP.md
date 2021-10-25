## Goal
The goal of this project is to look at historical data from Kickstarter projects, scraped by Web Robots at [link](https://webrobots.io/kickstarter-datasets/), and train and evaluate classification models that can predict if a campaign would most likely succeed or fail. This model can be used by Kickstarter as a paid or free service to entrepreneurs in order to evaluate likeliness of success of their projects. Increasing project success is in Kickstarter's interest as their revenue is taken from 5% of the successfully funded projects.

## Initial Findings
So far the bulk of the focus has been on EDA and cleaning the data so that it can be used for classification models. The data that has been explored has the following percentage of successful vs failed projects.

![Screen Shot 2021-10-25 at 2 11 16 PM](https://user-images.githubusercontent.com/47256224/138773798-720f1cac-187c-4469-920b-f8e9d04dfab1.png)

There were 39 attributes at the beginning which are limited to the following as of now:
- number of words in blurb
- number of words in name
- category
- subcategory
- country
- created at
- launched at
- deadline
- duration of project funding
- goal

The attributes are carefully chosen as the attributes that would be known at the beginning of each project campaign so that the entrepreneurs could use this model before starting the campaign if needed.

## Future work
There is still a need for limited process to be done on the project to clean and finalize the attributes that would be used for the model. After that the focus will be on modeling and evaluating different classification algorithms in order to choose the best performing model.

A list of the algorithms that may be tried are:
- KNN
- Logistic Regression
- Decision Tree, Random Forest
- XGBoost

The metrics to identify which model works the best will be:
- F1 score
- Confusion matrix
- ROC-AUC curve


