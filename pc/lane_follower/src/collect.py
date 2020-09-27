#!/usr/bin/env python3
from sys import exit
import rospy
import cv2
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import time

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

countdown(10)

print("starting......")

value = [0,0]
bridge = CvBridge()
training_data_image = []
training_data_val = []
train = []
rospy.init_node('collecter')
w = [2,0]
s = [-2,0]
a = [0,2]
d = [0,-2]
def vel_callback(vel):
    global value
    #print(value)
    if vel.linear.x == 2.0 and vel.angular.z == 0:
        value = w
    if vel.linear.x == -2.0 and vel.angular.z == 0:
        value = s
    if vel.linear.x == 0 and vel.angular.z == 2.0:
        value = a
    if vel.linear.x == 0 and vel.angular.z == -2.0 :
        value = d
    #training_data_val.append(value)

def img_callback(data):
    global value
    global training_data_image
    global training_data_val
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    training_data_image.append(cv_image)
    training_data_val.append(value)
    train.append([cv_image,value])
    print(len(training_data_val))
    if len(training_data_val) >= 500:
        np.save("data_image.npy",training_data_image)
        np.save("data_value.npy",training_data_val)
        #np.save("data.npy",train)
        print("saved the file exiting....")
        rospy.signal_shutdown("saved the file exiting....")
rospy.Subscriber("turtle1/cmd_vel",Twist,vel_callback)
rospy.Subscriber("rgb/image",Image,img_callback)
rospy.spin()

