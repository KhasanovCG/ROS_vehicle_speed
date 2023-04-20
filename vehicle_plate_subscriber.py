#I created another Python script 'vehicle_plate_subscriber.py' inside the scripts folder of the package. 
#In this script,I created a ROS subscriber that listens to the '/vehicle_speed' topic and echoes the plate number of the vehicle when its speed exceeds the speed limit value.
#I used the 'rospy.Subscriber()' method to create the subscriber and the 'rospy.get_param()' method to get the value of the 'speed_limit' parameter. 
#The code for the subscriber node is shown below

#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32, String

def vehicle_plate_subscriber():
    rospy.init_node('vehicle_plate_subscriber', anonymous=True)
    speed_limit = rospy.get_param('~speed_limit', 50) # km/h
    plate_number = rospy.get_param('~plate_number', 'UNKNOWN')
    rospy.Subscriber('/vehicle_speed', Float32, speed_callback, (speed_limit, plate_number))
    rospy.spin()

def speed_callback(speed_msg, args):
    speed_limit = args[0]
    plate_number = args[1]
    speed = speed_msg.data
    if speed > speed_limit:
        rospy.loginfo('Vehicle with plate number %s exceeded the speed limit (%d km/h)', plate_number, speed_limit)

if __name__ == '__main__':
    try:
        vehicle_plate_subscriber()
    except rospy.ROSInterruptException:
        pass


