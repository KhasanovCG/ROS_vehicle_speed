   autonomous_vehicle_speed

I created a new ROS package using the 'catkin_create_pkg' command in a terminal. 
I named the package 'autonomous_vehicle_speed' and include the 'rospy' and 'std_msgs' dependencies.
This is a ROS package that includes a publisher node that sends the speed of an autonomous vehicle and a subscriber node that
echoes the plate number of the vehicle when its speed exceeds the speed limit value.

   Requirements

ROS 
Python 2.7 or 3.x
std_msgs package

   Installation

1.Clone this repository into your catkin workspace:


cd /path/to/catkin_ws/src
git clone https://github.com/yourusername/autonomous_vehicle_speed.git

2.Build the package:


cd /path/to/catkin_ws
catkin_make


    Usage

1.Launch the 'autonomous_vehicle_speed' package:


roslaunch autonomous_vehicle_speed autonomous_vehicle_speed.launch

2.Check the output of the subscriber node in another terminal window:


rostopic echo /vehicle_speed

#This will show the plate number of the vehicle when its speed exceeds the speed limit value.

    Parameters
The following parameters can be set in the launch file 'autonomous_vehicle_speed.launch':

'speed_limit' (default: 60): The speed limit in kilometers per hour (K/H).
'plate_number' (default: "UNKNOWN"): The plate number of the autonomous vehicle.



