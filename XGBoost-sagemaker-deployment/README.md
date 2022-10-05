# Machine Learning Deployment using AWS SageMaker

## Table Of Contents

### Tutorials
* <b> Boston Housing (Batch Transform) - High Level </b> is the simplest notebook which introduces you to the SageMaker ecosystem and how everything works together. The data used is already clean and tabular so that no additional processing needs to be done. Uses the Batch Transform method to test the fit model.
* <b> Boston Housing (Batch Transform) - Low Level </b> performs the same analysis as the low level notebook, instead using the low level api. As a result it is a little more verbose, however, it has the advantage of being more flexible. It is a good idea to know each of the methods even if you only use one of them.
* <b> Boston Housing (Deploy) - High Level </b> is a variation on the Batch Transform notebook of the same name. Instead of using Batch Transform to test the model, it deploys and then sends the test data to the deployed endpoint.
* <b> Boston Housing (Deploy) - Low Level </b> is again a variant of the Batch Transform notebook above. This time using the low level api and again deploys the model and sends the test data to it rather than using the batch transform method.
* <b> IMDB Sentiment Analysis - XGBoost - Web App </b> creates a sentiment analysis model using XGBoost and deploys the model to an endpoint. Then describes how to set up AWS Lambda and API Gateway to create a simple web app that interacts with the deployed endpoint.
* <b> Boston Housing (Hyperparameter Tuning) - High Level </b> is an extension of the Boston Housing XGBoost model where instead of training a single model, the hyperparameter tuning functionality of SageMaker is used to train a number of different models, ultimately using the best performing model.
* <b> Boston Housing (Hyperparameter Tuning) - Low Level </b> is a variation of the high level hyperparameter tuning notebook, this time using the low level api to create each of the objects involved in constructing a hyperparameter tuning job.
* <b> Boston Housing - Updating an Endpoint </b> is another extension of the Boston Housing XGBoost model where in addition we construct a Linear model and switch a deployed endpoint between the two constructed models. In addition, we look at creating an endpoint which simulates performing an A/B test by sending some portion of the incoming inference requests to the XGBoost model and the rest to the Linear model.

### Mini-Projects
* <b> IMDB Sentiment Analysis - XGBoost (Batch Transform) </b> is a notebook that is to be completed which leads you through the steps of constructing a model using XGBoost to perform sentiment analysis on the IMDB dataset.
* <b> IMDB Sentiment Analysis - XGBoost (Hyperparameter Tuning) </b> is a notebook that is to be completed and which leads you through the steps of constructing a sentiment analysis model using XGBoost and using SageMaker's hyperparameter tuning functionality to test a number of different hyperparameters.
* <b> IMDB Sentiment Analysis - XGBoost (Updating a Model) </b> is a notebook that is to be completed and which leads you through the steps of constructing a sentiment analysis model using XGBoost and then exploring what happens if something changes in the underlying distribution. After exploring a change in data over time you will construct an updated model and then update a deployed endpoint so that it makes use of the new model.

### Project

<b> Sentiment Analysis Web App </b> is a notebook and collection of Python files to be completed. The result is a deployed RNN performing sentiment analysis on movie reviews complete with publicly accessible API and a simple web page which interacts with the deployed endpoint.

Using ml.t2.medium is a good idea as it is covered under the free tier. For the role, creating a new role works fine.