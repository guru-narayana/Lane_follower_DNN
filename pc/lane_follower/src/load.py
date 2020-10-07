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
    out = [0,0]
    im = image.reshape(150,100,1)
    prediction = np.array(model.predict([im]))
    print(prediction)
    out[0] = prediction[0][0]*2
    out[1] = prediction[0][1]*2+prediction[0][2]*(-2)
    print(prediction[0])
    return(out)
