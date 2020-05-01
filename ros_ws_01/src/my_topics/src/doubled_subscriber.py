#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from random import random # for random numbers!

def callback(msg):
    print 'doubled number:', msg.data           # print real part
    #print                             # blank line

rospy.init_node('doubled_subscriber') # initialize node

sub = rospy.Subscriber( # register subscription
  'doubled',            # topic
  Int32,              # custom type
  callback              # callback function
)

rospy.spin() # keep node running until shut down