from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData,PredictPipeline
#from src.logger import logging

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Airline=request.form.get('Airline'),
            Source=request.form.get('Source'),
            Destination=request.form.get('Destination'),
            Total_Stops=request.form.get('Total_Stops'),
            Journey_day=request.form.get('Journey_day'),
            Journey_month=request.form.get('Journey_month'),
            Journey_year=request.form.get('Journey_year'),
            hours=request.form.get('hours'),
            minutes=request.form.get('minutes'),
            Arrival_hour=request.form.get(' Arrival_hour'),
            Arrival_min=request.form.get(' Arrival_min'),
            duration_hours=request.form.get('duration_hours'),
            duration_mins=request.form.get('duration_mins'),

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(debug=True)        
    

