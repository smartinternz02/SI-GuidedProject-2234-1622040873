import numpy as np
from flask import Flask, request, jsonify, render_template
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "5hbBZ3uaGQTN74CAIulaseRJmg-0lK9UuvAoiZXBHw-X"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 18:03:28 2021

@author: Hari Prasad
"""

from flask import Flask ,render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open("regression.pkl",'rb'))
@app.route('/')
def intro():
    return render_template("index.html")
@app.route('/label',methods = ['POST']) # app is routed with the url '/' - localhost:5000
def label():
    
    cylinders = request.form["cylinder"]
    displacement = request.form["displacement"]
    horsepower = request.form["horsepower"]
    weight = request.form["weight"]
    acceleration = request.form["acceleration"]
    modelyear = request.form["modelyear"]
    origin = request.form["origin"]
    total = [[int(cylinders),int(displacement),int(horsepower),int(weight),int(acceleration),int(modelyear),int(origin)]]
    
    p = model.predict(total)
    p = p[0]
    print(p)
    return render_template('index.html',label = "The performance of the car is "+str(p))

if __name__=='__main__':
    app.run(debug = True,port = 9000)