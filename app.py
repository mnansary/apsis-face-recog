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
from deepface import DeepFace
# Define a flask app
app = Flask(__name__)


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
    similiarity_value=round(100- round(obj['distance']*100,2),2)
    return {"match":match,"similiarity %":similiarity_value}
    
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        response={}
        print(request.files.keys())
        if 'image1' not in request.files:
            response["error"]="image 1 not found"
            return jsonify(response)

        if 'image2' not in request.files:
            response["error"]="image 2 not found"
            return jsonify(response)
        
        # Save the file to ./uploads
        
        basepath = os.path.dirname(__file__)

        image1 = request.files['image1']
        src = os.path.join(basepath,'uploads', secure_filename(image1.filename))
        image1.save(src)

        image2 = request.files['image2']
        dst = os.path.join(basepath,'uploads', secure_filename(image2.filename))
        image2.save(dst)
        # match
        response=facematcher(src,dst)

        return jsonify(response)
    return None



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
