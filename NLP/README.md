# Facebook to Meta rebranding - A study of post announcement tweets

## Abstract
On October 28th, 2021, Facebook announced rebranding of the corporate name to Meta, in an effort to bring focus to the Metaverse, their project that introduces virtual and augmented reality technologies. This rebranding is also an effort to overhaul Facebook's public image in the recent years with a series of PR nightmares. The goal of this project is to study tweets including hashtags and keywords such as #Meta, #Metaverse, #Facebook, Zuckerberg for 8 days post announcment in order to extract topics and mine texts that were discussed by the public about this announcement. The proposed solution is an NMF topic modeling that groups the documents (tweets) into 50 topics, which can be helpful for further analysis such as EDA of number of tweets, likes and retweets per topic, as well as performing sentiment analysis on each topic.


## Data
About 405k original tweets were scraped from Twitter using Snscraper and the hashtags and keywords discussed above. Some initial cleaning of the dataframe included removing non-english and duplicate tweets, arriving at about 213k tweets for this analysis. The meta data includes date and time of tweet, user info, number of likes, retweets, but for topic modeling only user id and tweet content were extracted from the dataframe.


## Design
The design of this project started with scraping tweet data about the announcement in order to perform NLP and in specific topic modeling using NMF technique in order to group the tweets into specific tweets which can help with further study of the sentiment of tweets and topics that were part of the conversation. NMF was chosen as the technique since it generally performs better than LDA on short documents such as tweets. Number of topics (components) for NMF was tuned between 5 and 50 by qualitative comparison of the results, and 50 was chosen as the topic number as it extracted some more interesting topics from the tweets. After topic modeling, a preliminary EDA was done on number of tweets per some interesting topics extracted, as well as extracting most common words in those interesting topics.


## Algorithm
Python Pandas and Numpy was used for initial cleaning of the tabular data, scraped from twitter. Data was prepared for topic modeling by performing pre-processing tasks on the tweet content such as converting to lowercase, removing hashtags, links, audio and video contents, removing non-letter characters, removing stop words and lemmatizing and stemming the content after tokenizing the words in each content. Topic modeling was performed using pre-processed data and NMF technique and the number of components of NMF was tuned to 50. From the topic matrix, the topic with the highest probability was chosen as the topic of each document, allowing us to compare number of tweets per topic. Top words and tweets for some of the interesting topics were also extracted to interpret the topics further.

## Tools
- Python Pandas and Numpy for data exploration and pre-processing
- Scikit Learn, NLTK, Regex, Gensim for pre-processing
- Matplotlib, Seaborn and wordcloud for Data visualization

## Communication
[Here](https://github.com/atrinsarmadi/Metis_Projects/tree/main/NLP) is the slides and visulas presented at the end of the project.
