#!/usr/bin/env python

##modules imported
import rospy
from std_msgs.msg import Int32

##setup
rospy.init_node('doubler') # initialize node

## double the number recieved and then publish right away
def callback(msg):
    doubled = Int32()           # declare
    doubled.data = msg.data * 2 # double
    pub.publish(doubled)        # publish in callback!


## this node both recieves and sends data 
sub = rospy.Subscriber('counter', Int32, callback)
pub = rospy.Publisher('doubled', Int32, queue_size=3)

rospy.spin() # keep node running until shut down