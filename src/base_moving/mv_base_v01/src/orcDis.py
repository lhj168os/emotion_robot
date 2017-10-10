#!/usr/bin/env python
# license removed for brevity
# encoding: utf-8
from aip import AipOcr
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

def get_file_content (filePath):
    with open(filePath, 'rb') as fp: 
        return fp.read()

def img_ocr():                    
    APP_ID = '9417238'
    API_KEY = 'aiG3LGstm9AlTQnwGMxBfcA7'
    SECRET_KEY = '3GS8g9gB8afFHa7YhzfZogkcfdDz3n38'
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    try:
        result = aipOcr.general(get_file_content("res/img.jpg"))
        steps = int(result['words_result'][0]['words'])
        return steps
    except:
        return 0

def publisher_():
    pub = rospy.Publisher('ocrDis_cmd', Int32, queue_size=10)
    rospy.init_node('ocrDis', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        steps = img_ocr()
        rospy.loginfo(steps)
        pub.publish(steps)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher_()
    except rospy.ROSInterruptException:
        pass
