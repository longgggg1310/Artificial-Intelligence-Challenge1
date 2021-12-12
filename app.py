from flask import Flask, json, render_template, request,jsonify
import tensorflow as tf
from PIL import Image
from keras.preprocessing import image
import numpy as np
import base64
import cv2
app = Flask(__name__)
dic = {0:'umbrella',1:'banana',2:'grapes',3:'pineapple'}
# dic = {0:'cookie',1:'clock',2:'donut',3:'wheel'}

model = tf.keras.models.load_model('model.h5')
model.make_predict_function()


@app.route('/')

def index():

    return render_template('index.html')

@app.route('/recognize',methods=['POST'])
 


def regconize():
    if request.method == 'POST':
        data = request.get_json()
        imgBase64 = data['image']
        imgBytes = base64.b64decode(imgBase64) 
        with open('saved_picture/temp.jpg','wb') as temp:
            temp.write(imgBytes)
            
        image = cv2.imread('saved_picture/temp.jpg')
        image = cv2.resize(image,(28,28),interpolation=cv2.INTER_AREA)
        img_gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        img_prediction = np.reshape(img_gray,(1,28,28))
        print(img_prediction)
        print(model.predict(img_prediction))
        prediction = np.argmax(model.predict(img_prediction),axis=-1)
        return jsonify({
            'prediction' : str(dic[prediction[0]]),
            'status' :True
        })
        
        
    



if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
