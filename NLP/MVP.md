## Goal & Progress
The tweets were scraped using snscraper (SNS), a social media scraper tool in python. The decision to move away from Tweepy and use SNS instead came from the conclusion that SNS scrapes a lot more information/attributes than Tweepy, which can be useful at the later stages of this project. SNS also by default only scrapes original tweets (neglects re-tweets), which is more preferable for topic modeling process. The inital data was scraped using four hashtags: (#Zuckerberg, #Meta, #Metaverse, #Facebook) and included about 405k tweets and 28 attributes. After initial cleaning of data with processes such as removing duplicated contents and tweets from other languages than english, we are left with 213k tweets. 

The goal of this project is to look at tweets from 10/28/2021 when Facebook announced their name change to Meta, until 11/05/2021. The tweet contents will be used as part of a topic modeling process where the abstract/topics of the semantic behind the twitter contents will be discovered. This topic modeling and semantic analysis is helpful in discovering the reaction to Facebook name change to Meta, and the analysis can be used for future marketing purposes.

## Initial Topic Modeling
<img width="722" alt="Screen Shot 2021-11-08 at 2 52 45 PM" src="https://user-images.githubusercontent.com/47256224/140830998-188b8d63-6f7e-4006-8633-a7d20beeb18b.png">

At this point the topics are not a great representation of our analysis, first because more text preprocessing is necessary, and second reason is that the name of the company is used in a lot of texts, so these words need to be deleted from the documents.

## Future Steps
- Text preprocessing: such as changing contents to lower case, removing unneccesary punctuations, removing stop words, and perfroming lemmetization
- Topic Modeling using LDA
- If time: clustering

