# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:22:57 2021

@author: uday chowdary adusumilli
"""
## importing all required libraries

from flask import Flask, render_template, request

import warnings
warnings.filterwarnings('ignore')

import pandas as pd

##import the file from google colab similarity file

cosine_similarity_for_shoes = pd.read_csv('../DS18_PROJECT_04_UDAY_CHOWDARY_ADUSUMILLI/cosine_similarity_for_shoes.csv',index_col=[0])

app = Flask(__name__)
app.secret_key = 'iowngolcondafort'

##operations on web applications

@app.route('/view.html',methods=['POST', 'GET'])    
def similar_products():
    closest_imgs = " "
    closest_imgs_scores = " "
    given_img =" "
    if request.method == 'POST':
        given_img = request.form['given_img']
        
        closest_imgs = cosine_similarity_for_shoes[given_img].sort_values(ascending=False)[1:6].index
        closest_imgs_scores = cosine_similarity_for_shoes[given_img].sort_values(ascending=False)[1:6]
       
    return render_template('view.html',closest_imgs=closest_imgs,given_img=given_img,closest_imgs_scores=closest_imgs_scores)

if __name__ == '__main__':
    app.run(debug=False)
  