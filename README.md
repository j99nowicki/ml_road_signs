# ml_road_signs

Implementation of Road Signs Classifier using PyToarch CNN with STN. 

This is a Jupyter development project. 
To try the live deployment go here: https://rscwebapp.herokuapp.com
For web web project go to: https://github.com/j99nowicki/ml_road_signs_web

# The summary of the steps in this project

1.	Downloading and analysing GTSRB data
2.	Pre-processing data
3.	Researching for the best model and implementing CNN model with STN input
4.	Training the model on GPU
5.	Evaluation of the model metrics
6.	Training and evaluation of alternative transform learning model with ResNet18 on GPU

# Instructions for executing notebooks

Notebooks require two jupyter instances: CPU and GPU or just GPU, if cost is not a concern.

Notebooks should clone this github project. 

Notebooks and instances exchange some data via S3. I uploaded them later to public bucket so it is possible to run them out of order.

There are six notebooks in the project. First three notebooks should be run in sequence on CPU:

* CPU: 	1. Download data
* CPU: 	2. Prepare data 		-> pushes input data to S3 (copied manually to public bucket)

Remaining notebooks can be run in any order, but they follow a logical sequence:

* CPU: 	3. Inspect final data 	
* GPU: 	4. Load and train model -> pushes model parameters to S3 (disabled, the best	model parameters are already in public bucket)
* GPU: 	5. Transfer learning	
* CPU: 	6. Inference on cpu	
