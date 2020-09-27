#!/usr/bin/env python3
import cv2
import numpy as np
import rospy
import time
from load import predict_image
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
countdown(10)
bridge = CvBridge()
rospy.init_node('lane_automated', anonymous=True)
vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
vel = Twist()

def callback(data):
  cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
  gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
  v = predict_image(gray)
  vel.linear.x = v[0]
  vel.angular.z = v[1]
  vel_pub.publish(vel)
image_sub = rospy.Subscriber("/rgb/image",Image,callback)
rospy.spin()