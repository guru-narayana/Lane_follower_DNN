import cv2
import time
import numpy as np
from model import alexnet2
WIDTH = 150
HEIGHT = 100
lr = 1e-3
model = alexnet2(WIDTH,HEIGHT,lr,output=4)
model.load('final.model')
def predict_image(image):
    im = image.reshape(150,100,1)
    prediction = np.array(model.predict([im]))
    prediction = (prediction > 0.4)*1
    print(prediction[0])
    if (prediction[0] == [1,0,0,0]).all():
        return([2,0])
    elif(prediction[0] == [0,0,1,0]).all():
        return([0,-2])
    elif (prediction[0] == [0,1,0,0]).all():
        return([0,2])
    else:
        return([0,0])