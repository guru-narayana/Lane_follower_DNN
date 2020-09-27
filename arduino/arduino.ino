#include "ros.h"

#include "geometry_msgs/Twist.h"

float x; 
float a;
int l1 = 6;
int l2 = 5;
int r1 = 11;
int r2 = 10;
int left_value = 0;
int right_value = 0;
ros::NodeHandle nh;

void velCallback(  const geometry_msgs::Twist& vel)
{
     x = vel.linear.x;
     a = vel.angular.z;
     left_value = int(85*x);
     right_value = int(85*x);
     left_value+=int(a*85);
     right_value-= int(a*85);
     left_value = constrain(left_value, -255, 255);
     right_value = constrain(right_value, -255, 255);
     left_write(left_value);
     right_write(right_value);
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel" , velCallback);

void setup() {
     pinMode(l1,OUTPUT);
     pinMode(l2,OUTPUT);
     pinMode(r1,OUTPUT);
     pinMode(r2,OUTPUT);
     nh.initNode();
     nh.subscribe(sub);
}

void loop() {
     nh.spinOnce();
     digitalWrite(l1,LOW);
     digitalWrite(l2,LOW);
     digitalWrite(r1,LOW);
     digitalWrite(r2,LOW);
     delay(1);
}
void left_write(int left_value){
  if (left_value>0){
    analogWrite(l1,left_value);
    digitalWrite(l2,LOW);
  }else{
    analogWrite(l2,abs(left_value));
    digitalWrite(l1,LOW);
    }
}
void right_write(int right_value){
  if (right_value>0){
    analogWrite(r1,right_value);
    digitalWrite(r2, LOW);
   }
  else{
    analogWrite(r2,abs(right_value));
    digitalWrite(r1,LOW);
    }
}
