from flask import Flask,render_template,request
import os
# import tensorflow as tf
from PIL import Image
import numpy as np
import cv2
from keras.models import load_model
from werkzeug.utils import secure_filename
brain = Flask(__name__)
model=load_model('BrainTumor10Epochs2new1.h5')
print("model loadded check http://127.0.0.1:5000/")

def get_className(classno):
    if classno==0:
        return "No Brain tumor detected"
    elif classno==1:
        return "Brain tumor detected"
def getResult(img):
    image=cv2.imread(img)
    image=Image.fromarray(image)
    image=image.resize((256,256))

    input_img=np.expand_dims(image,axis=0)
    input_img = np.array(input_img)
    result=model.predict(input_img)
    return result

@brain.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@brain.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['file']
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(
            basepath,'pred',secure_filename(f.filename))
        f.save(file_path)
        print(file_path)
        value=getResult(file_path)
        result=get_className(value)
        return result
    return None



if __name__=='__main__':
    brain.run(debug=True)
