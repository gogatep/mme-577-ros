#!/usr/bin/env python

## importing modules
import rospy
from std_msgs.msg import Int32
from random import random # for random numbers!

## callback function to print the message received
def callback(msg):
    print 'doubled number:', msg.data           # print real part
    #print                             # blank line

## setup
rospy.init_node('doubled_subscriber') # initialize node

sub = rospy.Subscriber( # register subscription
  'doubled',            # topic
  Int32,              # custom type
  callback              # callback function
)


rospy.spin() # keep node running until shut down