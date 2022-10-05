# SageMaker Deployment Project

The notebook and Python files provided here, once completed, result in a simple web app which interacts with a deployed recurrent neural network performing sentiment analysis on movie reviews.

* <b> SageMaker Project.ipynb </b> leads through each of the steps and contains coding tasks and questions to complete
* <b> train </b> folder has the code for training the model
    * <b> train.py </b> is the training script to which you will make some modification
* <b> serve </b> folder has the code for the deployed the model
    * <b> predict.py </b> is the predicting script to which you will make some changes
* <b> website </b> folder has the code for interacting with the endpoint
    * <b> index.html </b> needs to be set up to work with your own endpoint