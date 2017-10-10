/*
*	Software：spark base moving
*	Author：Huanjie Liang
*	Time：3/15/2017
*	Version：0.0.0
*/


#include "ros/ros.h"
#include<sstream>
#include <geometry_msgs/Twist.h>      //The topic's data type of control spark
#include<std_msgs/Int32.h>       	  //The flag data type

std_msgs::Int32 Flag;                  //falg  
geometry_msgs::Twist speed_val;        //the speed variable of spark

/*
*	call-back function
*	get flag
*/
void chatterCallback(const std_msgs::Int32::ConstPtr& flag)
{
	Flag.data=flag->data;        //get the flag from 'base_control' topic
	ROS_INFO("%d", Flag.data);
	
	if(Flag.data == 1){            //forward
		speed_val.linear.x=1;      //linear speed    
	}else{ 						   //stop
		speed_val.linear.x=0;
	}
    speed_val.angular.z=0;         //angular speed
}


/*
*	main function
*
*/

int main(int argc, char **argv)
{
	ros::init(argc, argv, "listen");   			   //init the node
	ros::NodeHandle n;							   //instantiate a node handle
	ros::Subscriber sub = n.subscribe("base_control", 10, chatterCallback);          //listen "base_control" topic
	ros::Publisher cmd_vel_pub = n.advertise<geometry_msgs::Twist>("cmd_vel",100);   //publish to cmd_vel topic
	ros::Rate loop_rate(10);      //10 times/s
	
	while(ros::ok()){
		cmd_vel_pub.publish(speed_val);     //send the news to the "cmd_vel" topic
		ros::spinOnce();                    //publish once in a loop
		loop_rate.sleep();					//sleep
	}

	return 0;
}

