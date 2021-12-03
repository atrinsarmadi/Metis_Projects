# Image Classification of Traffic Signs

## Abstract
Self driving cars are inevitable. In recent years, there are lots of research and experiments to expedite the process of rolling out self driving cars in a larger scale. What makes a car a self driving car is a set of sensors and computers deployed on the car that gathers data from the surrounding of the car, processes the data to make decisions on how the car needs to be manuevered, and send control signals based on these decisions to the car controlling equipment using PID controllers.

Cameras are one of the main sensors deployed on these cars that gather image data from the surrounding. One of the main uses of cameras is to detect objects around the car. This project focuses on scenarios where those objects are traffic signs, and once the traffic sign objects are detected, we want to classify each traffic sign into the right category, which then will be used to make decisions on maneuvering. The goal is to use deep learning methods, mainly Convolutional Neural Networks (CNN) in order to train a model with traffic sign images and build this model so that it can classify traffic signs into the correct categories using images in a precise and rapid way. 


## DATA
The dataset is the German Traffic Sign Recognition Benchmark (GTSRB), downloaded from [here](https://benchmark.ini.rub.de). It includes 40k images of traffic signs from 43 different classes for training the model, and about 3k images for testing the model. 


## Design
Upon data acquisition and general EDA, a baseline model was created to examine the response of the study to a CNN model. The baseline is a simple CNN model which performed with 72% accuracy on the test data. To increase the accuracy, multiple CNN optimization methods with hyperparameter tuning were undertaken in order to study the optimum number of pooling layers and feature maps. Learning rate was also changed to a function of the number of epochs, in order to decrease the computation steps after each epoch. Since these model comparison experiments are computationally expensive, a set of normalization steps were performed to scale the pixel values. Best model from hyperparameter experiments was chosen as the final model trained, and tested on the test dataset, resulting in 99.2% accuracy.


## Algorithm
Here is the final CNN model architecture.
![model_FM](https://user-images.githubusercontent.com/47256224/144629309-f091453a-605b-47fc-9d0f-2cfacdce0f86.png)


## Tools
- h5py for working with binary files
- Python Pandas and Numpy for data exploration and pre-processing
- Keras as interface for designing and running CNN models
- Scikit Learn for further result analysis
- Matplotlib for Data visualization

## Communication
[Here](https://github.com/atrinsarmadi/Metis_Projects/tree/main/DeepLearning) are the slides and visulas presented at the end of the project.
