## Question

The goal of this project is to classify images of traffic signs into 43 categories. This image classification will be done using CNN methods and is useful in applications of self-driving cars, where the cameras installed on the car can take images/videos of the surrounding and use the classification of the traffic sign to prompt different signals to the car computer or control system.

## DATA

The dataset is the  German Traffic Sign Recognition Benchmark (GTSRB), downloaded from [here](https://benchmark.ini.rub.de). It includes 40k images of traffic signs from 43 different classes.

![Screen Shot 2021-11-29 at 2 42 00 PM](https://user-images.githubusercontent.com/47256224/143954951-5a4b47ad-0e41-48b3-9ded-45cf5f13f7fd.png)



## Initial Finding
Some initial EDA and a simple baseline CNN model was performed on the DATA to pre-analyze the feasibility of the project. The baseline model showed a 72% accuracy score on predicting the test data. Here is the baseline CNN model:

![Screen Shot 2021-11-29 at 2 42 16 PM](https://user-images.githubusercontent.com/47256224/143955227-9e3256e7-4dd1-489b-b9ed-1d6b9da16447.png)


## Future Work
1. Include more DATA either by transfer learning or by generating images to fix the class imbalance
2. Optimize the CNN model to increase accuracy score

