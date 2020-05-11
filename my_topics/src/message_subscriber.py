#!/usr/bin/env python

## import moduless
import rospy
from my_topics.msg import Complex

def callback(msg):# function to print message received
    print 'Real:', msg.real           # print real part
    print 'Imaginary:', msg.imaginary # print imag part
    print                             # blank line


## setup
rospy.init_node('message_subscriber') # initialize node

sub = rospy.Subscriber( # register subscription
  'complex',            # topic
  Complex,              # custom type
  callback              # callback function
)

rospy.spin() # keep node running until shut down