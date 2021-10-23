from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
file = open('model.pickle', 'rb')
model = pickle.load(file)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Income = int(request.form['Income'])
        Age=int(request.form['Age'])
        Experience=int(request.form['Experience'])
        CURRENT_JOB_YRS  =int(request.form['CURRENT_JOB_YRS'])
        CURRENT_HOUSE_YRS   =int(request.form['CURRENT_HOUSE_YRS'])
        single   = request.form['single']
        if(single=='single'):
            single=1
        else:
            single=0
        owned   =request.form['owned']
        if(owned=='owned'):
            owned=1
            rented=0
        elif(owned=='rented'):
             owned=0
             rented=1      
        else : 
             owned=0
             rented=0                    
        yes   =request.form['yes']
        if(yes=='yes'):
            yes=1
        else:
            yes=0       
        prediction=model.predict([[Income,Age,Experience,CURRENT_JOB_YRS,CURRENT_HOUSE_YRS,single,owned,rented,yes]]) 
        if prediction == 1:
            return render_template('index.html',prediction_text="The customer have high chance to default on loan")
        else:
            return render_template('index.html',prediction_text="The customer have low chance to default on loan")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

