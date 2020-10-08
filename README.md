# Lane_follower_DNN
lane follower made from scratch with raspberry pi and arduino, uses alex net for classification of the images.
rasperry folder corresponds to the package that you need install in the ros packages of rasperry pi and same goes for PC and arduino , here raspi uses serial communication 
to send velocity command to the arduino.
# Nodes ------>
 # 1.FOR COLLECTING THE DATA
    ![alt text](https://github.com/guru-narayana/Lane_follower_DNN/blob/master/pictures/collecting.png)
   As shown in the graph the nodes that u need to run to collect the traning data is collect.py in pc package which subcribes the /turtle1/cmd_vel topic and /rgb/image to get the 
   information about the velocity u gave at that perticular image and u need to use teleop keyboard node in turtle sim to control the robot while training.
 # 2.FOR TESTING 
    
