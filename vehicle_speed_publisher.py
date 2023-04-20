#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def vehicle_speed_publisher():
    rospy.init_node('vehicle_speed_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10 Hz
    speed_publisher = rospy.Publisher('/vehicle_speed', Float32, queue_size=10)
    speed = 0.0
    while not rospy.is_shutdown():
        # Get the speed of the vehicle
        # Replace this code with your own code to get the speed
        speed += 1.0

        # Publish the speed to the /vehicle_speed topic
        speed_publisher.publish(speed)

        rate.sleep()

if __name__ == '__main__':
    try:
        vehicle_speed_publisher()
    except rospy.ROSInterruptException:
        pass


# I created a Python script 'vehicle_speed_publisher.py' inside the scripts folder of the package.
# In this script, I created a ROS publisher that sends the speed of the autonomous vehicle to a topic named '/vehicle_speed'.
# I used the 'rospy.Publisher()' method to create the publisher and the 'rospy.Rate()' method to set the publishing rate. 
#The code for the publisher node is shown above