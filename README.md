
# Disaster Response Pipeline Project

### Project overview:
This project is to analyze disaster message data shared by Appen and build a model for a web app, which will classify upcoming disaster messages. The data shared by Appen contains messages collected during disaters and labels which group them into 32 categories. The web app will provide simply overview of input data along with a classifier which can be used to classify new messaged based on our trained model.

### File description:
data folder: 
Contains input message data: disaster_categories.csv disaster_messages.csv. The script process_data.py is used to pre-process the input data and write the cleaned dataframe into DisasterResponse.db, which will be further used when building the model.

models folder:
Contains a python script train_classifier.py to firstly read cleaned data saved in DisasterResponse.db, followed by building a training model. The trained model will be saved in classifier.pkl file. Due to the size limit of git, this .pkl file is not uploaded here.

app folder:
Contains a main python script and html templates for the web app. Simply run the python script as described in below 'Instructions' section to view the web app by going to http://0.0.0.0:3002/ in your browser.

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3002/


