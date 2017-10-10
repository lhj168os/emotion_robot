#include "ros/ros.h"
#include <sstream>
#include <std_msgs/Int32.h>

std_msgs::Int32 cm;

void stepDis_(const std_msgs::Int32::ConstPtr& step)
{
	cm.data = step->data;
	ROS_INFO("receive: %d",cm.data);
}


int main(int argc, char **argv)
{
	int step = 2;
	ros::init(argc, argv, "stepDis");
	ros::NodeHandle n;
	ros::Publisher stepDis_pub = n.advertise<std_msgs::Int32>("base_control",2);
	ros::Subscriber stepDis_sub = n.subscribe("ocrDis_cmd", 3, stepDis_);
	ros::Rate loop_rate(10);
	while(ros::ok())
	{
		std_msgs::Int32 flag;
		flag.data = 0;
		if(cm.data == step){
			stepDis_pub.publish(flag);
			step++;
		}
		if(cm.data == 5) break;
		ros::spinOnce();
		loop_rate.sleep();
	}

	return 0;
}
