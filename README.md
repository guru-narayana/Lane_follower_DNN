# Lane_follower_DNN
lane follower made from scratch with raspberry pi and arduino, uses alex net for classification of the images.
rasperry folder corresponds to the package that you need install in the ros packages of rasperry pi and same goes for PC and arduino , here raspi uses serial communication 
to send velocity command to the arduino.
# NODES ------>
 1.For Collecting The Data
 
 ![alt text](https://github.com/guru-narayana/Lane_follower_DNN/blob/master/pictures/collecting.png)
   
   As shown in the graph the nodes that u need to run to collect the traning data is collect.py in pc package which subcribes the /turtle1/cmd_vel topic and /rgb/image to get the 
   information about the velocity u gave at that perticular image and u need to use teleop keyboard node in turtle sim to control the robot while training.
 
 
 
 2.For Training & Testing
    In order to train the i used the alexnetv2 for which code is there in the PC folderand you can choose the model depending on the complexity of the images you
    and also you might have to use transfer learning to fit data into a model which wasnt desgined for that.in terms of GPU i recommed to use googlecolab(its pretty fast). 
    
 ![alt text](https://github.com/guru-narayana/Lane_follower_DNN/blob/master/pictures/test_run.png)    
    
    
    
    In the testing phase u need to load the saved model (change the path in the load.py) and use main .py node to test the model it publishes linear and angular velocity based on 
    float output of the  model, if u have no way of controlling with pwm (in the case of controlling motor with raspberry directly) u can use threshhold of the probablity to
    determine the direction


# Publishing the images RaspberryPi
   I faced many issues while installing cv_bridge in RaspberryPi model3b so i had to use the source code of the cv_bridge image to images_msg conversin and published 
   the image u can use the same code for publishing the images.
