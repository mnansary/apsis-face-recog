#-*- coding: utf-8 -*-
"""
@author:MD.Nazmuddoha Ansary
"""
from __future__ import print_function
import sys
import os
import glob
import re
import numpy as np

# Flask utils
from flask import Flask, redirect, url_for, request, render_template,jsonify
from werkzeug.utils import secure_filename
# models

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Define a flask app
app = Flask(__name__)

from deepface import DeepFace
def facematcher(src,dest):
    '''
        matches two given faces:
        args:
            src     :   path of first image
            dest    :   path of second image
            return_dict :   if set to True returns a dictionary of {match,similiarity} 
    '''
    obj=DeepFace.verify(src,dest,model_name = 'ArcFace', detector_backend = 'retinaface')
    
    match=obj["verified"]
    similiarity_value=100- round(obj['distance']*100,2)
    return {"match":match,"similiarity":similiarity_value}
    
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,"tests",'uploads', secure_filename(f.filename))
        f.save(file_path)

        response=ocr.extract(file_path)
        return jsonify(response)
    return None


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
