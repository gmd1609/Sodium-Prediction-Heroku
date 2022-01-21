
from typing import Text
from flask import Flask, render_template, request
#import jsonify 
import requests 
import pickle
import numpy as np
import pandas as pd
import sklearn
app = Flask(__name__)
model = pickle.load(open('Support_Vector_Machine.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    Gender = request.form.get('Gender')
    age = request.form.get('age')
    Daily_Sodium_intake = request.form.get('Daily Sodium intake')
    Hypertension = request.form.get('Hypertension')
    if(Gender=='Male'):
        Gender=1
    elif (Gender=='Female'):
        Gender=0
    if(age=='14 and above'):
        age=0
    elif (age=='9 to 13'):
        age=1
    elif (age=='2 to 3'):
        age=2
    elif (age=='4 to 8'):
        age=3
    if(Hypertension=='No'):
        Hypertension=0
    elif (Hypertension=='Yes'):
        Hypertension=1
  
    output = model.predict([[ Gender, age, Daily_Sodium_intake, Hypertension]])
    if output == 2300:
        res_val = "** Normal sodium consumption **"
    elif output == 1900:
        res_val = "** Normal sodium consumption **"
    elif output == 1500:
        res_val = "** High sodium consumption **"
    elif output == 2200:
        res_val = "** High sodium consumption **"
    else:
        res_val = "** Sodium Consumption Is Not High, Not Normal **"

    return render_template('index.html', prediction_text='{}'.format(res_val))

if __name__=="__main__":
    app.run(debug=True)
